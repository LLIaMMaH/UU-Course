# -*- coding: utf-8 -*-

from typing import Union


def get_matrix(n: int = 1, m: int = 10, value: Union[int, str] = None):
    if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0:
        return []

    matrix = []

    for _ in range(n):
        row = [value] * m
        matrix.append(row)

    return matrix


if __name__ == "__main__":
    result1 = get_matrix(2, 2, 10)
    result2 = get_matrix(3, 5, 42)
    result3 = get_matrix(4, 2, 13)
    result4 = get_matrix(3, 3, 'Приветик')

    print(result1)
    print(result2)
    print(result3)
    print(result4)
