# -*- coding: utf-8 -*-

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    string = string.upper()
    for item in list_to_search:
        if string == item.upper():
            return True
    return False


if __name__ == "__main__":
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
    print(calls)
