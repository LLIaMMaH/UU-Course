# -*- coding: utf-8 -*-

def ask_number(prompt: str) -> int:
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print('Ошибка: Введите целое число.')


def get_numbers() -> list:
    while True:
        num_count = ask_number('Введите количество чисел: ')
        if num_count <= 1:
            print('Для сравнения нужно минимум два числа.')
            continue
        break

    numbers = []
    for i in range(num_count):
        num = ask_number(f'Введите число {i + 1}: ')
        numbers.append(num)
    return numbers


def check_equal_numbers(numbers_list: list) -> int:
    if not numbers_list:
        return 0

    if len(set(numbers_list)) == 1:
        return len(numbers_list)

    counts = {}
    for num in numbers_list:
        counts[num] = counts.get(num, 0) + 1

    max_count = 0

    for num in counts:
        if counts[num] > max_count:
            max_count = counts[num]

    if max_count >= 2:
        return max_count
    else:
        return 0


if __name__ == "__main__":
    numbers = get_numbers()
    equal_count = check_equal_numbers(numbers)
    print(f'Одинаковых чисел: {equal_count}')
