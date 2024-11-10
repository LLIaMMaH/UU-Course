# -*- coding: utf-8 -*-

def task_1() -> None:
    homework_count = 12
    hours_spent = 1.5
    course_name = 'Python'
    one_task = hours_spent / homework_count

    # Как просят по заданию
    print('Курс:', course_name, 'всего задач:', homework_count, 'затрачено часов:', hours_spent,
          'среднее время выполнения:', one_task, 'часа.')

    # Как мне нравится
    print(f'Курс: {course_name}, всего задач: {homework_count}, затрачено часов: {hours_spent}, среднее время выполнения \
{one_task} часа.')


if __name__ == "__main__":
    task_1()
