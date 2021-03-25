# -*- coding: utf-8 -*-
# Author: github.com/madhavajay

import ast
import sys
from typing import Any, Generator, List, Tuple, Type

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


# By using PEP 3102 -- Keyword-Only Arguments we can force all args named
# after the * to require invocation with the explicit name

MSG = "FKO100 Non Keyword-Only Arguments not allowed. Try adding a '*'."


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int, str]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa FKO100
        if len(node.args.args) >= 1:
            if len(node.args.args) == 1 and (
                node.args.args[0].arg == "self"
                or node.args.args[0].arg == "cls"  # noqa E501
            ):
                # allowed
                pass
            else:
                self.problems.append((node.lineno, node.col_offset, MSG))

        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, *, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(node=self._tree)
        for (
            line,
            col,
            msg,
        ) in visitor.problems:
            yield line, col, msg, type(self)
