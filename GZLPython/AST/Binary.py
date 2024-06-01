from ..Token import Token
from typing import Any

class Binary:
     def __init__(self, left: Any, operator: Token, right: Any):
        self.left = left
        self.operator = operator
        self.right = right
