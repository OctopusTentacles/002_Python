
import random

class House:
    def __init__(self):
        self.fridge = 50
        self.money = 0


class Person:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 50

    def eat(self):
        if self.house.fridge > 0:
            self.satiety += 10
            self.house.fridge -= 10
            print(f'{self.name} поел.')

    def work(self):
        self.satiety -= 10
        self.house.money += 50
        print(f'{self.name} поработал.')

    def play(self):
        self.satiety -= 10
        print(f'{self.name} поиграл.')

    def shop(self):
        if self.house.money >= 10:
            self.house.fridge += 20
            self.house.money -= 20
            print(f'{self.name} сходил в магазин.')

