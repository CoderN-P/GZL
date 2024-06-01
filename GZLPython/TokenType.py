from enum import Enum


class TokenType(Enum):
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    COMMA = 5
    DOT = 6
    MINUS = 7
    PLUS = 8
    TILDA = 9
    RATIO = 10
    STAR = 11
    SEMICOLON = 12
    BANG = 13
    BANG_EQUAL = 14
    EQUAL = 15
    EQUAL_EQUAL = 16
    LESS = 17
    LESS_EQUAL = 18
    GREATER = 19
    GREATER_EQUAL = 20
    IDENTIFIER = 21
    STRING = 22
    NUMBER = 23
    # Keywords
    CAP = 24
    NOCAP = 25
    SUS = 26
    MORESUS = 27
    ORELSE = 28
    RIZZUP = 29
    DROP = 30
    VIBE = 31
    RIZZ = 32
    NAH = 33
    YAP = 34
    ALSO = 35
    EOF = 36
