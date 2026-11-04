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
    def execute(self, script, action, timeout, cancelled):
        command = build_command(timeout)
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
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
                        raise SandboxError(
                            "Sandbox-Prozess wurde unerwartet beendet."
                        )
                    continue
                data = os.read(process.stdout.fileno(), 4096)
                if not data:
                    raise SandboxError("Sandbox lieferte keine Abschlussmeldung.")
                buffer.extend(data)
                while b"\n" in buffer:
                    raw, _, remainder = buffer.partition(b"\n")
                    buffer = bytearray(remainder)
                    if len(raw) > MAX_PROTOCOL_LINE:
                        raise SandboxError("Sandbox-Protokollzeile zu gross.")
                    message = json.loads(raw)
                    if message.get("type") == "action":
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
                        except Exception as error:
                            result = {"type": "result", "id": count,
                                      "ok": False, "error": str(error)[:2000]}
                        self._send(process, result)
                    elif message.get("type") == "result":
                        if message.get("ok"):
                            return True, ""
                        error = message.get("error", "Skriptfehler")
                        line = message.get("line")
                        location = f" (Zeile {line})" if line else ""
                        error_type, separator, detail = error.partition(": ")
                        message = detail if separator else error
                        return False, f"{error_type}{location}: {message}"
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
