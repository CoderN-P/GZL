from typing import List
from .Token import Token
from .TokenType import TokenType


class Scanner:
    keywords: dict[str, TokenType] = {
        'also': TokenType.ALSO,
        'cap': TokenType.CAP,
        'drop': TokenType.DROP,
        'more sus': TokenType.MORESUS,
        'nah': TokenType.NAH,
        'nocap': TokenType.NOCAP,
        'orelse': TokenType.ORELSE,
        'rizz': TokenType.RIZZ,
        'rizzup': TokenType.RIZZUP,
        'sus': TokenType.SUS,
        'vibe': TokenType.VIBE,
        'yap': TokenType.YAP,
        'ratio': TokenType.RATIO,
    }

    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()

        match c:
            case '(':
                self.add_token(TokenType.LEFT_PAREN)
            case ')':
                self.add_token(TokenType.RIGHT_PAREN)
            case '{':
                self.add_token(TokenType.LEFT_BRACE)
            case '}':
                self.add_token(TokenType.RIGHT_BRACE)
            case ',':
                self.add_token(TokenType.COMMA)
            case '.':
                self.add_token(TokenType.DOT)
            case '-':
                self.add_token(TokenType.MINUS)
            case '+':
                self.add_token(TokenType.PLUS)
            case ';':
                self.add_token(TokenType.SEMICOLON)
            case '*':
                self.add_token(TokenType.STAR)
            case '!':
                if self.match('='):
                    self.add_token(TokenType.BANG_EQUAL)
                else:
                    self.add_token(TokenType.BANG)
            case '=':
                if self.match('='):
                    self.add_token(TokenType.EQUAL_EQUAL)
                else:
                    self.add_token(TokenType.EQUAL)
            case '<':
                if self.match('='):
                    self.add_token(TokenType.LESS_EQUAL)
                else:
                    self.add_token(TokenType.LESS)
            case '>':
                if self.match('='):
                    self.add_token(TokenType.GREATER_EQUAL)
                else:
                    self.add_token(TokenType.GREATER)
            case '~':
                if self.match('~'):
                    self.multiline_comment()
                else:
                    while self.peek() != '\n' and not self.end():
                        self.advance()
            case ' ' | '\r' | '\t':
                pass
            case '\n':
                self.line += 1
            case '"':
                self.string()
            case _:
                if c.isdigit():
                    self.number()
                elif c.isalpha() or c == '_':
                    self.identifier()
                else:
                    print(f'[{self.line}] Error: Unexpected character "{c}"')

    def multiline_comment(self):
        while not (self.peek() == '~' and self.peekNext() == '~') and not self.end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.end():
            print(f'[{self.line}] Error: Unterminated comment.')

        self.advance()
        if self.end():
            print(f'[{self.line}] Error: Unterminated comment.')
        self.advance()

    def identifier(self):
        while self.peek().isalnum():
            self.advance()

        text = self.code[self.start:self.current]

        if 'yap' in text:
            print(repr(text))

        token_type = self.keywords.get(text, TokenType.IDENTIFIER)

        if token_type == TokenType.IDENTIFIER:
            self.add_token(TokenType.IDENTIFIER, text)
        else:
            self.add_token(token_type)

    def peek(self):
        if self.end():
            return '\0'
        return self.code[self.current]

    def string(self):
        while self.peek() != '"' and not self.end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.end():
            print(f'[{self.line}] Error: Unterminated string.')
            return

        print(self.code[self.current + 1])
        self.advance()

        value = self.code[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def add_token(self, type, literal=None):
        text = self.code[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == '.' and self.peekNext().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.code[self.start:self.current]))

    def peekNext(self):
        if self.current + 1 >= len(self.code):
            return '\0'
        return self.code[self.current + 1]

    def match(self, expected):
        if self.end():
            return False
        if self.code[self.current] != expected:
            return False

        self.current += 1
        return True

    def advance(self):
        self.current += 1
        return self.code[self.current - 1]

    def end(self) -> bool:
        return self.current >= len(self.code)
