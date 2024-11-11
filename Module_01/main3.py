# -*- coding: utf-8 -*-

def task_1() -> None:
    example = 'А роза упала на лапу Азора'
    print(example[0])
    print(example[-1])
    print(example[(len(example) - 1) // 2:])
    print(example[::-1])
    print(example[::2])


if __name__ == "__main__":
    task_1()
