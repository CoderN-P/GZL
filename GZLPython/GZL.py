from .utils import get_file
from . import Scanner


class GZL:
    had_error = False

    def __init__(self, **kwargs):
        if kwargs.get('file'):
            self.run(get_file(kwargs.get('file')))

    def run(self, code):
        scanner = Scanner(code)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    def error(self, line, message, col=None):
        print(f'[{line}] Error: {message}')
        self.had_error = True

