import unittest
from pathlib import Path


class ModulGroessenTests(unittest.TestCase):
    def test_python_dateien_bleiben_bei_hoechstens_150_zeilen(self):
        project = Path(__file__).resolve().parents[1]
        source_files = (
            path for path in project.rglob("*.py")
            if ".venv" not in path.parts and "__pycache__" not in path.parts
        )
        too_large = []
        for path in source_files:
            line_count = len(path.read_text(encoding="utf-8").splitlines())
            if line_count > 150:
                too_large.append((path.relative_to(project), line_count))
        self.assertEqual(too_large, [])


if __name__ == "__main__":
    unittest.main()
