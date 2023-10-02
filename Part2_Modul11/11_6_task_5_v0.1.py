
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
