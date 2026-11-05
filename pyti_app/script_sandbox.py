"""Linux bubblewrap runner for untrusted learner scripts."""

import json
import os
import select
import subprocess
import time

from .script_sandbox_command import SandboxError, build_command, child_limits

MAX_PROTOCOL_LINE = 65536
MAX_ACTIONS = 10000


class LinuxScriptSandbox:
    def execute(self, script, action, timeout, cancelled, telemetry=None):
        command = build_command(timeout)
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0,
            close_fds=True,
            start_new_session=True,
            env={"PATH": "/usr/bin:/bin", "HOME": "/tmp", "TMPDIR": "/tmp"},
        )
        deadline = time.monotonic() + timeout
        buffer = bytearray()
        count = 0
        try:
            self._send(process, {
                "script": script,
                "limits": child_limits(timeout),
                "telemetry": telemetry is not None,
            })
            while True:
                if cancelled.is_set():
                    raise InterruptedError("Skriptausfuehrung abgebrochen.")
                if time.monotonic() >= deadline:
                    raise TimeoutError("Skript-Zeitlimit ueberschritten.")
                ready, _, _ = select.select(
                    [process.stdout], [], [], min(0.05, deadline - time.monotonic())
                )
                if not ready:
                    if process.poll() is not None:
                        raise self._unexpected_exit(
                            process, "Sandbox-Prozess wurde unerwartet beendet"
                        )
                    continue
                data = os.read(process.stdout.fileno(), 4096)
                if not data:
                    raise self._unexpected_exit(
                        process, "Sandbox lieferte keine Abschlussmeldung"
                    )
                buffer.extend(data)
                while b"\n" in buffer:
                    raw, _, remainder = buffer.partition(b"\n")
                    buffer = bytearray(remainder)
                    if len(raw) > MAX_PROTOCOL_LINE:
                        raise SandboxError("Sandbox-Protokollzeile zu gross.")
                    message = json.loads(raw)
                    if message.get("type") == "trace":
                        if telemetry and not cancelled.is_set():
                            telemetry(
                                "line", line=message["line"],
                                variables=message.get("variables", {}),
                            )
                    elif message.get("type") == "action":
                        count += 1
                        if count > MAX_ACTIONS or message.get("id") != count:
                            raise SandboxError("Ungueltige Pyti-Aktionsfolge.")
                        name = message.get("name")
                        if name not in (
                            "moveForward", "turnLeft", "turnRight", "turnAround",
                            "pickBeeper", "dropBeeper", "jump", "onBeeper",
                            "beeperAhead", "frontClear", "leftClear",
                            "rightClear", "anyBeeperInBag",
                        ):
                            raise SandboxError("Unbekannte Pyti-Aktion.")
                        try:
                            value = action(name)
                            result = {"type": "result", "id": count,
                                      "ok": True, "value": value}
                            if telemetry:
                                telemetry("action", name=name, result=value,
                                          line=message.get("line"),
                                          variables=message.get("variables", {}))
                        except Exception as error:
                            result = {"type": "result", "id": count,
                                      "ok": False, "error": str(error)[:2000]}
                        self._send(process, result)
                    elif message.get("type") == "result":
                        if message.get("ok"):
                            return True, ""
                        response = message
                        error = response.get("error", "Skriptfehler")
                        line = response.get("line")
                        location = f" (Zeile {line})" if line else ""
                        error_type, separator, detail = error.partition(": ")
                        display_message = detail if separator else error
                        if telemetry:
                            telemetry(
                                "error", message=error,
                                traceback=response.get("traceback", error),
                                **({"line": line} if line else {}),
                            )
                        return False, f"{error_type}{location}: {display_message}"
                    else:
                        raise SandboxError("Ungueltige Sandbox-Antwort.")
                if len(buffer) > MAX_PROTOCOL_LINE:
                    raise SandboxError("Sandbox-Protokollzeile zu gross.")
        except TimeoutError:
            raise
        except (BrokenPipeError, OSError, ValueError, json.JSONDecodeError) as error:
            raise SandboxError(f"Sandbox-Kommunikation fehlgeschlagen: {error}") from error
        finally:
            self._stop(process)
            process.stdin.close()
            process.stdout.close()
            process.stderr.close()

    @staticmethod
    def _send(process, message):
        data = json.dumps(message, separators=(",", ":")).encode() + b"\n"
        if len(data) > MAX_PROTOCOL_LINE:
            raise SandboxError("Sandbox-Anfrage zu gross.")
        process.stdin.write(data)
        process.stdin.flush()

    @staticmethod
    def _stop(process):
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=0.25)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)

    @staticmethod
    def _unexpected_exit(process, message):
        process.wait()
        detail = process.stderr.read(4096).decode(
            "utf-8", errors="replace"
        ).strip()
        suffix = f": {detail}" if detail else ""
        return SandboxError(f"{message}{suffix}.")
