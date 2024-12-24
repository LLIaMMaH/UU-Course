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


if __name__ == "__main__":
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
