from .utils import get_file
from . import Scanner
from .TokenType import TokenType
from .Parser import Parser
from .Interpreter import Interpreter
from .ASTPrinter import ASTPrinter


class GZL:
    had_error = False

    def __init__(self, **kwargs):
        if kwargs.get('file'):
            self.run(get_file(kwargs.get('file')))

    def run(self, code):
        scanner = Scanner(code)
        tokens = scanner.scan_tokens()
        interpreter = Interpreter()
        parser = Parser(tokens)
        statements = parser.parse()

        if not statements:
            return

        interpreter.interpret(statements)



    @staticmethod
    def error(token, message):
        if token.token_type == TokenType.EOF:
            GZL.report(token.line, "at end", message)

        else:
            GZL.report(token.line, token.lexeme, message)

    @staticmethod
    def report(line, where, message):
        print(f'\n[line {line}] Error {where}: {message}')
        GZL.had_error = True




