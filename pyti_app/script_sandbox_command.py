"""Builds the fail-closed bubblewrap invocation and child resource limits."""

import shutil
import sys
import sysconfig
from pathlib import Path

MULTIARCH = sysconfig.get_config_var("MULTIARCH")
RUNTIME_LIBRARIES = (
    Path("/lib64"),
    Path("/usr/lib64"),
    *((Path(root) / MULTIARCH for root in ("/lib", "/usr/lib"))
      if MULTIARCH else ()),
)


class SandboxError(RuntimeError):
    """The isolated script runner could not safely execute a script."""


def build_command(timeout):
    bwrap = shutil.which("bwrap")
    if not sys.platform.startswith("linux") or not bwrap:
        raise SandboxError(
            "Sichere Skriptausfuehrung erfordert Linux und bubblewrap."
        )
    args = [
        bwrap, "--die-with-parent", "--new-session",
        "--unshare-all", "--unshare-user", "--disable-userns",
        "--assert-userns-disabled", "--cap-drop", "ALL",
        "--size", str(32 * 1024 * 1024), "--tmpfs", "/",
        "--size", str(64 * 1024 * 1024), "--tmpfs", "/tmp",
        "--dev", "/dev", "--proc", "/proc",
        "--dir", "/etc", "--dir", "/home", "--dir", "/root",
        "--clearenv", "--setenv", "HOME", "/tmp", "--setenv", "TMPDIR",
        "/tmp", "--setenv", "PATH", "",
        "--setenv", "PYTHONDONTWRITEBYTECODE", "1",
    ]
    prefix = Path(sys.base_prefix).resolve()
    python = Path(sys.executable).resolve()
    if not prefix.is_dir() or not python.is_file():
        raise SandboxError("Die aktive Python-Laufzeit ist nicht erreichbar.")
    home = Path.home().resolve()
    if prefix == Path("/") or prefix == home or prefix in home.parents:
        raise SandboxError(
            "Die Python-Laufzeit liegt in einem zu weit gefassten Verzeichnis."
        )
    _create_mount_parents(args, prefix)
    args.extend(["--ro-bind", str(prefix), str(prefix)])
    for library_dir in RUNTIME_LIBRARIES:
        if library_dir.is_dir():
            resolved_library_dir = library_dir.resolve()
            if resolved_library_dir != prefix and not resolved_library_dir.is_relative_to(prefix):
                _create_mount_parents(args, library_dir)
                args.extend(["--ro-bind", str(resolved_library_dir),
                             str(library_dir)])
    if not python.is_relative_to(prefix):
        _create_mount_parents(args, python)
        args.extend(["--ro-bind", str(python), str(python)])
    runner = Path(__file__).with_name("sandbox_child.py").read_text(
        encoding="utf-8"
    )
    args.extend([
        "--chdir", "/tmp", "--", python, "-I", "-S", "-c", runner,
    ])
    return args


def _create_mount_parents(args, path):
    for parent in reversed(path.parents):
        if str(parent) == "/":
            continue
        args.extend(["--dir", str(parent)])


def child_limits(timeout):
    return {
        "RLIMIT_CPU": max(1, int(timeout)),
        "RLIMIT_AS": 1024 * 1024 * 1024,
        "RLIMIT_FSIZE": 16 * 1024 * 1024,
        "RLIMIT_NOFILE": 64,
        "RLIMIT_NPROC": 8,
        "RLIMIT_CORE": 0,
    }
