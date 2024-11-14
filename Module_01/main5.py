# -*- coding: utf-8 -*-

def task_1() -> None:
    immutable_var = (10, 20, 30, "Слово", "Два слова", 3.14, True, [1, 2, 3])
    print(immutable_var)

    try:
        immutable_var[0] = 20
    except TypeError as e:
        print(f"Ошибка: {e}")
        if type(immutable_var) == tuple:
            print("Кортежи в Python являются неизменяемыми (immutable) структурами данных. Это означает, что после \
создания кортежа его элементы не могут быть изменены. Попытка изменить элемент кортежа приводит к ошибке \
TypeError.")


def task_2() -> None:
    mutable_list = [1, 2, 3, "Мир", "Труд", "Май", 5.6, False]
    print(mutable_list)

    mutable_list[3] = "Май"
    mutable_list[5] = "Мир"
    print(mutable_list)

if __name__ == "__main__":
    task_1()
    task_2()
