from typing import Any

from GZLPython.Expr import Visitor, Binary, Unary, Grouping, Literal
from GZLPython.Token import Token
from GZLPython.TokenType import TokenType


class RPN(Visitor):
    def __init__(self):
        expression = Binary(
            Binary(
                Literal(1),
                Token(TokenType.PLUS, '+', None, 1),
                Literal(2)
            ),
            Token(TokenType.STAR, '*', None, 1),
            Binary(
                Literal(4),
                Token(TokenType.MINUS, '-', None, 1),
                Literal(3)
            )
        )

        print(self.print_tree(expression))

    def print_tree(self, expression):
        return expression.accept(self)

    def visit_literal_expr(self, expr: Literal) -> Any:
        if not expr.value:
            return "nah"

        return expr.value

    def visit_unary_expr(self, expr: Unary) -> Any:
        return f'{expr.right.accept(self)} {expr.operator.lexeme}'

    def visit_binary_expr(self, expr: Binary) -> Any:
        return f'{expr.left.accept(self)} {expr.right.accept(self)} {expr.operator.lexeme}'

    def visit_grouping_expr(self, expr: Grouping) -> Any:
        return expr.expression.accept(self)


printer = RPN()

