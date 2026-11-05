"""Runs the local developer suite and emits machine-readable case results."""

import json
import sys
import unittest
from pathlib import Path


_RESULT_MARKER = "PYTI_TEST_RESULT:"


class AdminTestResult(unittest.TextTestResult):
    def _report(self, test, status):
        identifier = test.id()
        if "(" in identifier and identifier.endswith(")"):
            class_id = identifier.split("(", 1)[1][:-1]
        else:
            class_id = identifier.rsplit(".", 1)[0]
        print(
            _RESULT_MARKER + json.dumps({
                "id": identifier,
                "class": class_id,
                "status": status,
            }),
            flush=True,
        )

    def addSuccess(self, test):
        super().addSuccess(test)
        self._report(test, "OK")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._report(test, "FAIL")

    def addError(self, test, err):
        super().addError(test, err)
        self._report(test, "ERROR")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._report(test, f"ÜBERSPRUNGEN: {reason}")

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None:
            self._report(test, "FAIL")


class AdminTestRunner(unittest.TextTestRunner):
    resultclass = AdminTestResult


def main():
    project_root = Path(sys.argv[1]).resolve()
    test_root = project_root / "tests"
    if not test_root.is_dir():
        print(f"Testverzeichnis nicht gefunden: {test_root}", file=sys.stderr)
        return 2
    sys.path[:0] = [str(test_root), str(project_root)]
    suite = unittest.defaultTestLoader.discover(
        str(test_root), pattern="test_*.py", top_level_dir=str(test_root)
    )
    result = AdminTestRunner(verbosity=0).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
