# -*- coding: utf-8 -*-

def task_1() -> None:
    my_string = input("Введите произвольную строку: ")
    len_string = len(my_string)
    print(f'Длинна введёной строки: {len_string}')
    print(f'Ваша строка в верхнем регистре: {my_string.upper()}')
    print(f'Ваша строка в нижнем регистре: {my_string.lower()}')
    print(f'Ваша строка без пробелов: {my_string.replace(" ", "")}')
    print(my_string[0])
    print(my_string[-1])


if __name__ == "__main__":
    task_1()
