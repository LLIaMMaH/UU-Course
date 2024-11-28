# -*- coding: utf-8 -*-
from typing import Any


def print_params(a: Any = 1, b: Any = 'Строка', c: Any = True) -> None:
    """
    Не указывать тип входящих параметров, так себе тема.
    """
    print(f'Параметры имеют значения: a = {a} | b = {b} | c = {c}')


if __name__ == "__main__":
    print_params()
    print_params(b=25)
    print_params(c=[1, 2, 3])

    values_list = [True, 3.14, 'Это строка в параметре "c"']
    values_dict = {'a': 1, 'b': 2, 'c': 3}
    print_params(*values_list)
    print_params(**values_dict)

    values_list_2 = [54.32, 'Строка с текстом']
    print_params(*values_list_2, 42)
