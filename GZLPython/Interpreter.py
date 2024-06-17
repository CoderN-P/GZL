from typing import Any
from . import Expr
from . import Stmt
from .Expr import Literal, Grouping, Unary, Binary, Variable, Assignment
from .Stmt import Print, Var
from .TokenType import TokenType
from .Environment import Environment


class Interpreter(Expr.Visitor, Stmt.Visitor):
    def __init__(self):
        self.environment = Environment()

    def interpret(self, statements):
        for statement in statements:
            self.execute(statement)

    def execute(self, stmt):
        return stmt.accept(self)

    def visit_expr_stmt(self, stmt: Stmt.Expr) -> Any:
        self.evaluate(stmt.expression)
        return None

    def visit_assignment_expr(self, expr: Assignment) -> Any:
        value = self.evaluate(expr.value)

        self.environment.assign(expr.name, value)
        return value

    def visit_print_stmt(self, stmt: Print) -> Any:
        value = self.evaluate(stmt.expression)
        print(str(value))
        return None

    def visit_literal_expr(self, expr: Literal) -> Any:
        return expr.value

    def visit_grouping_expr(self, expr: Grouping) -> Any:
        return self.evaluate(expr.expression)

    def visit_unary_expr(self, expr: Unary) -> Any:
        right = self.evaluate(expr.right)

        match expr.operator.token_type:
            case TokenType.MINUS:
                return -right
            case TokenType.BANG:
                return self.truthy(right)

    def visit_binary_expr(self, expr: Binary) -> Any:
        right = self.evaluate(expr.right)
        left = self.evaluate(expr.left)

        match expr.operator.token_type:
            case TokenType.RATIO:
                return left / right
            case TokenType.STAR:
                return right * left
            case TokenType.MINUS:
                return left - right
            case TokenType.PLUS:
                return right + left
            case TokenType.GREATER:
                return left > right
            case TokenType.GREATER_EQUAL:
                return left >= right
            case TokenType.EQUAL_EQUAL:
                return self.equal(right, left)
            case TokenType.LESS:
                return left < right
            case TokenType.LESS_EQUAL:
                return left <= right
            case TokenType.BANG_EQUAL:
                return not self.equal(right, left)
        return None

    def visit_var_stmt(self, stmt: Var) -> Any:
        value = None

        if stmt.initializer is not None:
            value = self.evaluate(stmt.initializer)

        self.environment.define(stmt.name.lexeme, value)
        return None

    def visit_variable_expr(self, expr: Variable) -> Any:
        return self.environment.get(expr.name)

    def equal(self, obj1, obj2):
        return obj1 == obj2

    def truthy(self, obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return obj
        return True

    def evaluate(self, expr):
        return expr.accept(self)
