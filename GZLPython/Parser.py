from .TokenType import TokenType
from .Expr import Binary, Unary, Literal, Grouping, Variable, Assignment
from .Stmt import Print, Expr, Var


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []

        while not self.end():
            statements.append(self.declaration())

        return statements

    def declaration(self):
        try:
            if self.match(TokenType.LIT):
                return self.variable_declaration()
            return self.statement()
        except Exception as e:
            print(e)
            exit(65)

    def synchronize(self):
        pass

    def variable_declaration(self):
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name")

        initializer = None

        if self.match(TokenType.EQUAL):
            initializer = self.expression()

        self.consume(TokenType.SEMICOLON, "Expect ';' after variable declaration")
        return Var(name, initializer)

    def statement(self):
        if self.match(TokenType.YAP):
            return self.print_statement()

        return self.expression_statement()

    def print_statement(self):
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after value.")
        return Print(value)

    def expression_statement(self):
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after value.")
        return Expr(expr)

    def expression(self):
        return self.assignment()

    def assignment(self):
        expr = self.equality()

        if self.match(TokenType.EQUAL):
            equals = self.previous()
            value = self.assignment()

            if isinstance(expr, Variable):
                name = expr.name
                return Assignment(name, value)
            else:
                self.error(equals, "Invalid assignment target.")

        return expr

    def equality(self):
        expr = self.comparison()

        while self.match(TokenType.EQUAL_EQUAL, TokenType.BANG_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def match(self, *args):
        for token in args:
            if self.check(token):
                self.advance()
                return True
        return False

    def check(self, token_type):
        if self.end():
            return False
        return self.peek().token_type == token_type

    def advance(self):
        if not self.end():
            self.current += 1

        return self.previous()

    def end(self):
        return self.peek().token_type == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def comparison(self):
        expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()

        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.match(TokenType.STAR, TokenType.RATIO):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            expr = Unary(operator, right)
            return expr

        return self.primary()

    def primary(self):
        if self.match(TokenType.CAP):
            return Literal(False)
        if self.match(TokenType.NOCAP):
            return Literal(True)
        if self.match(TokenType.NAH):
            return Literal(None)
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)
        if self.match(TokenType.IDENTIFIER):
            return Variable(self.previous())
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
            return Grouping(expr)

        return self.error(self.peek(), "Expect Expression")

    def consume(self, token_type, error):
        if self.check(token_type):
            return self.advance()

        return self.error(self.peek(), error)

    @staticmethod
    def error(token, msg):
        from .GZL import GZL
        GZL.error(token, msg)
        raise RuntimeError
