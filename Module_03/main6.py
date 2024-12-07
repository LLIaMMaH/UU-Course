# -*- coding: utf-8 -*-

def calculate_sum_and_length(item):
    """Вариант 1"""
    if isinstance(item, (list, tuple)):
        sum_numbers = 0
        sum_string_lengths = 0
        for element in item:
            n, l = calculate_sum_and_length(element)
            sum_numbers += n
            sum_string_lengths += l
        return sum_numbers, sum_string_lengths

    elif isinstance(item, dict):
        sum_numbers = 0
        sum_string_lengths = 0
        for key, value in item.items():
            n_key, l_key = calculate_sum_and_length(key)
            n_value, l_value = calculate_sum_and_length(value)
            sum_numbers += n_key + n_value
            sum_string_lengths += l_key + l_value
        return sum_numbers, sum_string_lengths

    elif isinstance(item, str):
        return 0, len(item)

    elif isinstance(item, (int, float)):
        return item, 0

    elif isinstance(item, set):
        sum_numbers = 0
        sum_string_lengths = 0
        for element in item:
            n, l = calculate_sum_and_length(element)
            sum_numbers += n
            sum_string_lengths += l
        return sum_numbers, sum_string_lengths

    else:
        return 0, 0


def sum_all(data):
    """Вариант 2"""
    total = 0
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(k, str):
                total += len(k)
            elif isinstance(k, (int, float)):
                total += k
            total += sum_all(v)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += sum_all(item)
    elif isinstance(data, str):
        total += len(data)
    elif isinstance(data, (int, float)):
        total += data
    return total


# Исходная структура данных
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

if __name__ == "__main__":
    # Вариант 1
    # Вычисление суммы чисел и длин строк
    total_numbers, total_string_lengths = 0, 0
    for element in data_structure:
        # print(element)
        n, l = calculate_sum_and_length(element)
        total_numbers += n
        total_string_lengths += l
        # print(n, l)

    # Общая сумма
    total_sum = total_numbers + total_string_lengths

    print(f"Сумма всех чисел: {total_numbers}")
    print(f"Сумма длин всех строк: {total_string_lengths}")
    print(f"Общая сумма: {total_sum}")

    # Вариант 2
    print(sum_all(data_structure))
