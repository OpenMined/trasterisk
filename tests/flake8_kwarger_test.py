# -*- coding: utf-8 -*-
# Author: github.com/madhavajay

import ast
from typing import Set

from flake8_kwarger import Plugin

example_1 = """class A:
    @staticmethod
    def foo_bad(forcenamed):
        print(forcenamed)

    @staticmethod
    def foo_good(*, forcenamed):
        print(forcenamed)

    def bar_bad(self, forcenamed):
        print(self, forcenamed)

    def bar_good(self, *, forcenamed):
        print(self, forcenamed)
"""


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f"{line}:{col + 1} {msg}" for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results("") == set()


def test_missing_kwargs_only():
    ret = _results(example_1)
    msg = "FKO100 Non Keyword-Only Arguments not allowed. Try adding a '*'."
    expected = {
        f"3:5 {msg}",
        f"10:5 {msg}",
    }
    assert ret == expected
