# -*- coding: utf-8 -*-
# Author: github.com/madhavajay

import ast
import os
from pathlib import Path
from typing import Set

from flake8_kwarger import Plugin


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f"{line}:{col + 1} {msg}" for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results("") == set()


def test_missing_kwargs():
    examples_dir = Path(os.path.dirname(__file__)) / ".." / "examples"
    example_file = examples_dir / "example.py"
    with open(example_file) as f:
        example = "".join(f.readlines())

    ret = _results(example)
    msg = "FKO100 Non Keyword-Only Arguments not allowed. Try adding a '*'."

    expected = {
        f"3:5 {msg}",
        f"10:5 {msg}",
    }
    assert ret == expected
