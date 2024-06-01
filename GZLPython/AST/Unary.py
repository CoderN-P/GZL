from ..Token import Token
from typing import Any

class Unary:
     def __init__(self, operator: Token, right: Any):
        self.operator = operator
        self.right = right
