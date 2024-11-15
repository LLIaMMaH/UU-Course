# -*- coding: utf-8 -*-

from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU')


def fake_data(rows: int = 10) -> None:
    values_str = ''
    for i in range(rows):
        first_name_nonbinary = fake.first_name_nonbinary()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80)

        values_str += f'"{first_name_nonbinary}": "{date_of_birth}"'
        if (i + 1) < rows:
            values_str += ', '
    print(values_str)


def task_1() -> None:
    my_dict = {"Никандр": "1991-08-16", "Пантелеймон": "1946-06-03", "Сократ": "1974-06-26", "Лазарь": "2004-11-04",
               "Мирон": "1980-08-16", "Ерофей": "1975-09-01", "Кондрат": "1952-09-03", "Валентин": "1982-10-30",
               "Ипатий": "2006-01-25", "Твердислав": "2005-10-14"}
    print(f'Dict: {my_dict}')

    print(f'Existing value: {my_dict["Мирон"]}')
    print(f'Not existing value: {my_dict.get("Александр")}')

    my_dict.update({"Алина": "1985-10-31", "Пелагея": "1992-11-28"})
    print(f'Modified dictionary: {my_dict}')

    get_person = my_dict.pop('Ерофей')
    print(f'Deleted value: {get_person}')

    print(f'Final change: {my_dict}')


def task_2() -> None:
    my_set = {1, 2, 3, "Мир", "Труд", "Мир", 5.6, False, True, 3, 2, 1, "Труд"}
    print(f'Set: {my_set}')

    my_set.add(5)
    my_set.add("Май")
    print(f'Modified set: {my_set}')


if __name__ == "__main__":
    # fake_data()
    task_1()
    print('\n' * 2 + '=' * 30 + '\n' * 2)
    task_2()
