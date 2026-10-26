"""Formatting of learner script errors for the application status."""

import traceback


def format_script_error(error):
    line = getattr(error, "lineno", None)
    if line is None:
        frames = traceback.extract_tb(error.__traceback__)
        line = next(
            (frame.lineno for frame in reversed(frames)
             if frame.filename == "<pyti-script>"),
            None,
        )
    location = f" (Zeile {line})" if line is not None else ""
    message = getattr(error, "msg", str(error))
    return f"{type(error).__name__}{location}: {message}"
