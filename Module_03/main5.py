# -*- coding: utf-8 -*-

def get_multiplied_digits(number: int) -> str:
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    return first



if __name__ == "__main__":
    result = get_multiplied_digits(40203)
    print(result)

    # Умножение на 0 даст 0
    result2 = get_multiplied_digits(402030)
    print(result2)
