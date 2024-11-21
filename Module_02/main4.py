# -*- coding: utf-8 -*-

def task_1() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    primes = []
    not_primes = []

    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
            else:
                not_primes.append(num)

    print(f'Primes: {primes}')
    print(f'Not Primes: {not_primes}')


if __name__ == "__main__":
    task_1()
