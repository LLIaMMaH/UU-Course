# -*- coding: utf-8 -*-

def task_1() -> None:
    grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
    students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
    sort_students = sorted(students)
    stud_dict = dict(zip(sort_students, grades))

    avg_dict = {}
    for k, v in stud_dict.items():
        avg_dict[k] = sum(v) / len(v)
    print(avg_dict)

if __name__ == "__main__":
    task_1()
