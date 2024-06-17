import os


def generate_ast(output_dir):
    define_ast(
        output_dir,
        "Expr",
        [
            'Binary   - left: Any, operator: Token, right: Any',
            'Grouping - expression: Any',
            'Literal  - value: Any',
            'Unary    - operator: Token, right: Any',
            'Variable - name: Token',
            'Assignment - name: Token, value: Any'
        ]
    )
    define_ast(
        output_dir,
        "Stmt",
        [
            "Block - statements: Any"
            "Expr  - expression: Any",
            "Print - expression: Any",
            "Var - name: Any, initializer: Any"
        ]
    )


def define_ast(output_dir, base_name, types):
    path = f'{output_dir}'

    if not os.path.exists(path):
        os.makedirs(path)

    with open(f'{path}/{base_name}.py', 'w') as f:
        f.write('from .Token import Token\n')
        f.write('from abc import ABC, abstractmethod\n')
        f.write('from typing import Any\n\n\n')
        f.write(f'class {base_name}(ABC):\n')
        f.write('    @abstractmethod\n')
        f.write(f'    def accept(self, visitor: Any) -> Any:\n')
        f.write('        pass\n\n\n')

        for t in types:
            class_name = t.split('-')[0].strip()
            fields = t.split('-')[1].strip()
            define_type(f, class_name, base_name, fields)

        define_visitor(f, base_name, types)


def define_visitor(f, base_name, types):
    f.write('class Visitor(ABC):\n')

    for t in types:
        type_name = t.split('-')[0].strip()
        f.write(f'    @abstractmethod\n')
        f.write(f'    def visit_{type_name.lower()}_{base_name.lower()}(self, {base_name.lower()}: {type_name}) -> Any:\n')
        f.write('        pass\n\n')

def define_type(f, base_name, parent_name, fields):

    f.write(f'class {base_name}({parent_name}):\n')
    f.write(f'    def __init__(self, {fields}):\n')

    for field in fields.split(', '):
        name = field.split(': ')[0]
        f.write(f'        self.{name} = {name}\n')

    f.write('\n')

    f.write('    def accept(self, visitor: Any) -> Any:\n')
    f.write(f'        return visitor.visit_{base_name.lower()}_{parent_name.lower()}(self)\n\n')
    f.write('\n')


generate_ast('GZLPython')
