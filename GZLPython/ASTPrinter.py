from typing import Any

from GZLPython.Expr import Visitor, Expr, Literal, Grouping, Binary, Unary
from GZLPython.TokenType import TokenType
from GZLPython.Token import Token


class ASTPrinter(Visitor):

    def print_tree(self, expr: Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: Binary):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_literal_expr(self, expr: Literal) -> Any:
        if expr.value is None:
            return "nah"
        return str(expr.value)

    def visit_grouping_expr(self, expr: Grouping):
        return self.parenthesize('group', expr.expression)

    def visit_unary_expr(self, expr: Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr):
        s = '(' + name

        for expression in exprs:
            s += ' '
            s += expression.accept(self)

        s += ')'

        return s



