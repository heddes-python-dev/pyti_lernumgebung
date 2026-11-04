"""Restricted child process entry point used inside the Linux sandbox."""

import json
import os
import resource
import sys
import traceback

MAX_LINE = 65536


def send(message):
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
        send({"type": "action", "id": sequence, "name": command})
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
        })


run()
