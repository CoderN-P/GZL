def generate_ast():
    define_ast(
        [
            'Binary   - left: Any, operator: Token, right: Any',
            'Grouping - expression: Any',
            'Literal  - value: Any',
            'Unary    - operator: Token, right: Any',
        ]
    )


def define_ast(types):
    for t in types:
        class_name = t.split('-')[0].strip()
        fields = t.split('-')[1].strip()
        define_type(class_name, fields)

def define_type(base_name, fields):
    path = f'./AST/{base_name}.py'

    with open(path, 'w') as f:
        f.write('from ..Token import Token\n')
        f.write('from typing import Any\n\n')
        f.write(f'class {base_name}:\n ')

        # Constructor
        f.write(f'    def __init__(self, {fields}):\n')

        for field in fields.split(', '):
            print(field)
            name = field.split(': ')[0]
            f.write(f'        self.{name} = {name}\n')


generate_ast()
