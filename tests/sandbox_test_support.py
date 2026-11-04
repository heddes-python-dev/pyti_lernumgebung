import threading
from functools import lru_cache

from pyti_app.script_sandbox import LinuxScriptSandbox
from pyti_app.script_sandbox_command import SandboxError


@lru_cache(maxsize=1)
def sandbox_unavailable_reason():
    try:
        success, error = LinuxScriptSandbox().execute(
            "pass", lambda _name: None, 3, threading.Event()
        )
    except SandboxError as exception:
        if "Failed RTM_NEWADDR: Operation not permitted" in str(exception):
            return "Runner does not permit bubblewrap's isolated network namespace."
        if "erfordert Linux und bubblewrap" in str(exception):
            return "Linux bubblewrap is unavailable."
        raise
    if not success:
        raise AssertionError(f"Sandbox smoke test failed: {error}")
    return None
