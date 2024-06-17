class Environment:
    def __init__(self, enclosing=None):
        self._values = {}
        self.enclosing = enclosing

    def define(self, name, value):
        self._values[name] = value

    def get(self, name):
        if name.lexeme in self._values:
            return self._values[name.lexeme]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise RuntimeError(name, f"Undefined variable: '{name.lexeme}'.")

    def assign(self, name, value):
        if name.lexeme in self._values:
            self._values[name.lexeme] = value
            return

        if self.enclosing is not None:
            return self.enclosing.assign(name, value)

        raise RuntimeError(name, f"Undefined variable: '{name.lexeme}'.")