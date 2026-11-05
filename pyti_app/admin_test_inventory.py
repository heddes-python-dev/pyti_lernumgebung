"""Discover developer test methods without importing or executing them."""

import ast
from pathlib import Path


def load_test_cases(test_root):
    cases = []
    for path in sorted(Path(test_root).glob("test_*.py")):
        module = path.stem
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            class_id = f"{module}.{node.name}"
            cases.extend(
                (f"{class_id}.{method.name}", class_id, module, method.name)
                for method in node.body
                if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef))
                and method.name.startswith("test_")
            )
    return cases

