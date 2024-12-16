# -*- coding: utf-8 -*-

def test_function() -> None:
    def inner_function() -> None:
        print('Я в области видимости функции test_function')

    inner_function()


if __name__ == "__main__":
    test_function()

    # 4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
    inner_function()
