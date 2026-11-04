import os
import shutil
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from pyti_app.script_sandbox import LinuxScriptSandbox
from pyti_app.script_sandbox_command import SandboxError, build_command


class SandboxFailClosedTests(unittest.TestCase):
    def test_missing_linux_sandbox_prevents_execution(self):
        with patch("pyti_app.script_sandbox_command.sys.platform", "win32"):
            with patch("pyti_app.script_sandbox_command.shutil.which", return_value=None):
                with self.assertRaises(SandboxError):
                    build_command(5)

    def test_root_wide_python_prefix_is_rejected(self):
        with patch("pyti_app.script_sandbox_command.sys.platform", "linux"):
            with patch("pyti_app.script_sandbox_command.shutil.which",
                       return_value="/usr/bin/bwrap"):
                with patch("pyti_app.script_sandbox_command.sys.base_prefix", "/"):
                    with self.assertRaisesRegex(SandboxError, "zu weit"):
                        build_command(5)


@unittest.skipUnless(
    sys.platform.startswith("linux") and shutil.which("bwrap"),
    "Linux and bubblewrap are required for sandbox tests.",
)
class LinuxScriptSandboxTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = LinuxScriptSandbox()

    def execute(self, script, timeout=5):
        return self.sandbox.execute(
            script, lambda _name: None, timeout, threading.Event()
        )

    def test_isolation_hides_home_blocks_host_writes_and_network(self):
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "host-marker"
            marker.write_text("unchanged", encoding="utf-8")
            host_netns = os.stat("/proc/self/ns/net").st_ino
            script = (
                "import os\n"
                "import socket\n"
                "from pathlib import Path\n"
                f"assert not Path({str(Path.home() / '.config')!r}).exists()\n"
                f"assert not Path({str(marker)!r}).exists()\n"
                "assert os.stat('/proc/self/ns/net').st_ino != "
                f"{host_netns}\n"
                "connection = socket.socket()\n"
                "connection.settimeout(0.3)\n"
                "try:\n"
                "    connection.connect(('1.1.1.1', 53))\n"
                "except OSError:\n"
                "    pass\n"
                "else:\n"
                "    raise AssertionError('Network is reachable')\n"
                "finally:\n"
                "    connection.close()\n"
                "Path('/tmp/pyti-sandbox-marker').write_text('sandbox')\n"
                "Path('/etc/passwd').write_text('sandbox')\n"
                "assert Path('/etc/passwd').read_text() == 'sandbox'\n"
            )
            self.assertEqual(self.execute(script), (True, ""))
            self.assertEqual(marker.read_text(encoding="utf-8"), "unchanged")
            self.assertFalse(Path("/tmp/pyti-sandbox-marker").exists())

    def test_script_errors_keep_their_type_and_line(self):
        success, error = self.execute("moveForward()\nraise ValueError('bad')")

        self.assertFalse(success)
        self.assertIn("ValueError (Zeile 2): bad", error)

    def test_timeout_terminates_an_infinite_loop(self):
        with self.assertRaises(TimeoutError):
            self.execute("while True:\n    pass", timeout=2)


if __name__ == "__main__":
    unittest.main()
