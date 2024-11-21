# -*- coding: utf-8 -*-

def task_1() -> None:
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    while len(my_list) != 0:
        value = my_list.pop(0)
        if value > 0:
            print(value)
        elif value == 0:
            continue
        else:
            break


if __name__ == "__main__":
    task_1()
