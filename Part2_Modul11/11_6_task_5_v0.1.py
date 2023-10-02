
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

    def live_one_day(self):
        action_dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.fridge < 10:
            self.shop()
        elif self.house.money < 50:
            self.work()
        elif action_dice == 1:
            self.work()
        elif action_dice == 2:
            self.eat()
        else:
            self.play()

        if self.satiety <= 0:
            raise ValueError(f'{self.name} умер от голода!')


house = House()
person1 = Person('Artem', house)
person2 = Person('Alice', house)

for day in range(365):
    print(f'--- День {day + 1} ---')
    person1.live_one_day()
    person2.live_one_day()
    print(f'В доме осталось {house.fridge} еды и {house.money} денег.')