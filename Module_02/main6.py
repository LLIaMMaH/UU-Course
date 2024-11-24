# -*- coding: utf-8 -*-

def find_password(num: int) -> str:
    result = ''
    for i in range(1, 21):
        for j in range(i, 21):
            if (i + j) != 0 and num % (i + j) == 0:
                result += str(i) + str(j) + ' '
    return result


while True:
    try:
        number = int(input("Введите число от 3 до 20 (0 для выхода): "))
        if number ==0:
            break
        elif 3 <= number <= 20:
            password = find_password(number)
            if password != '':
                print(f'Все возможные пароли: {password}')
            else:
                print('Подходящие пароли не найдены.')
        else:
            print('Неверное число. Пожалуйста, введите число от 3 до 20.')
    except ValueError:
        print('Неверный ввод. Пожалуйста, введите целое число.')
