# -*- coding: utf-8 -*-

class House:
    def __init__(self, name: str, number_of_floor: int):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor: int):
        if self.number_of_floor < new_floor or new_floor > self.number_of_floor:
            print('Такого этажа не существует')
        else:
            self.number_of_floor = new_floor
            print(self.number_of_floor)

    def __str__(self):
        return f'НазваниеЖ {self.name}, количество этажей: {self.number_of_floor}'

    def __len__(self):
        return self.number_of_floor


if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(len(h1))
    print(len(h2))
