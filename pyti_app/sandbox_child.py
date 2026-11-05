"""Restricted child process entry point used inside the Linux sandbox."""

import json
import os
import resource
import sys
import traceback

MAX_LINE = 65536


def json_value(value, depth=0):
    if value is None or isinstance(value, (bool, int, float, str)):
        return value if not isinstance(value, str) or len(value) <= 500 else value[:497] + "..."
    if depth >= 3:
        return f"<{type(value).__name__}>"
    if isinstance(value, (list, tuple, set)):
        return [json_value(item, depth + 1) for item in list(value)[:100]]
    if isinstance(value, dict):
        return {
            str(key)[:100]: json_value(item, depth + 1)
            for key, item in list(value.items())[:100]
            if isinstance(key, (str, int, float, bool))
        }
    return f"<{type(value).__name__}>"


def variables(frame):
    return {
        name: json_value(value)
        for name, value in list(frame.f_locals.items())[:100]
        if not name.startswith("__") and not callable(value)
    }


def send(message):
    data = json.dumps(message, separators=(",", ":")).encode() + b"\n"
    if len(data) > MAX_LINE:
        if message.get("type") in ("trace", "action"):
            message["variables"] = {}
            data = json.dumps(message, separators=(",", ":")).encode() + b"\n"
        if len(data) > MAX_LINE:
            data = b'{"type":"result","ok":false,"error":"Antwort zu gross"}\n'
    os.write(1, data)


def set_limit(name, value):
    resource.setrlimit(getattr(resource, name), (value, value))


def run():
    channel_in = sys.stdin.buffer
    request = json.loads(channel_in.readline(MAX_LINE))
    for name, value in request["limits"].items():
        set_limit(name, value)
    sys.stdin = open(os.devnull, encoding="utf-8")
    sys.stdout = sys.__stdout__ = open(os.devnull, "w", encoding="utf-8")
    sys.stderr = sys.__stderr__ = sys.stdout
    commands = (
        "moveForward", "turnLeft", "turnRight", "turnAround",
        "pickBeeper", "dropBeeper", "jump", "onBeeper", "beeperAhead",
        "frontClear", "leftClear", "rightClear", "anyBeeperInBag",
    )
    sequence = 0

    def invoke(command):
        nonlocal sequence
        sequence += 1
        message = {"type": "action", "id": sequence, "name": command}
        if request.get("telemetry"):
            frame = sys._getframe(1)
            while frame.f_code.co_filename != "<pyti-script>":
                frame = frame.f_back
            message.update(line=frame.f_lineno, variables=variables(frame))
        send(message)
        response = json.loads(channel_in.readline(MAX_LINE))
        if response.get("id") != sequence or response.get("type") != "result":
            raise RuntimeError("Ungueltige Antwort vom Pyti-Prozess.")
        if not response.get("ok"):
            raise RuntimeError(response.get("error", "Pyti-Aktion fehlgeschlagen."))
        return response.get("value")

    namespace = {
        command: (lambda command=command: invoke(command))
        for command in commands
    }
    try:
        code = compile(request["script"], "<pyti-script>", "exec")

        def trace(frame, event, _arg):
            if frame.f_code.co_filename == "<pyti-script>":
                if event == "line":
                    send({
                        "type": "trace", "line": frame.f_lineno,
                        "variables": variables(frame),
                    })
                return trace
            return None

        if request.get("telemetry"):
            sys.settrace(trace)
            try:
                exec(code, namespace, namespace)
            finally:
                sys.settrace(None)
        else:
            exec(code, namespace, namespace)
        send({"type": "result", "ok": True})
    except BaseException as error:
        line = next(
            (
                frame.lineno
                for frame in reversed(traceback.extract_tb(error.__traceback__))
                if frame.filename == "<pyti-script>"
            ),
            getattr(error, "lineno", None),
        )
        send({
            "type": "result",
            "ok": False,
            "error": f"{type(error).__name__}: {str(error)[:2000]}",
            "line": line,
            "traceback": traceback.format_exc()[-2000:],
        })


run()
