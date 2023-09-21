# Задача 05. Совместное проживание
# Что нужно сделать
# Чтобы понять, стоит ли ему жить с кем-то или всё же лучше остаться в 
# гордом одиночестве, Артём решил провести довольно необычное исследование. 
# Для этого он реализовал модель человека и модель дома.

# Человек может (должны быть такие методы):

# есть (+ сытость, − еда); работать (− сытость, + деньги); играть (− сытость); 
# ходить в магазин за едой (+ еда, − деньги); 
# прожить один день (выбирает одно действие согласно описанному ниже 
# приоритету и выполняет его).

# У человека есть (должны быть такие атрибуты):
# имя,
# степень сытости (изначально 50),
# дом.

# В доме есть:
# холодильник с едой (изначально 50 еды),
# тумбочка с деньгами (изначально 0 денег).
# Если сытость человека становится меньше нуля, человек умирает.

# Логика действий человека определяется следующим образом: 
# Генерируется число кубика от 1 до 6. Если сытость < 20, то нужно поесть. 
# Иначе, если еды в доме < 10, то сходить в магазин. 
# Иначе, если денег в доме < 50, то работать. 
# Иначе, если кубик равен 1, то работать.
# Иначе, если кубик равен 2, то поесть. Иначе играть.

# По такой логике эксперимента человеку надо прожить 365 дней.

# Реализуйте такую программу и создайте двух людей, живущих в одном доме. 
# Проверьте работу программы несколько раз.


import random


class House:
    def __init__(self):
        self.fridge = 50
        self.money = 0

    def info(self):
        print(f'еды: {self.fridge:<10}'
              f'денег: {self.money:<10}'
              f'сытость: {Human.satiety:<10}')


class Human:
    def __init__(self, name, satiety):
        self.name = name
        self.satiety = satiety
        
    def year(self):
        
        for day in range(1, 6):
            print(f'\n\033[0;32mДень {day}:\033[0m')
            house.info()

            cube_number = random.randint(1, 6)
            
            if self.satiety < 0:
                print(f'{self.name} умирает.')
                break
            elif self.satiety < 20:
                print(f'Нужно поесть!', end=' ')
                self.to_eat(cube_number)

            elif cube_number == 1:
                self.to_work(cube_number)

                


    def to_eat(self, cube_number):
        self.satiety += cube_number
        house.fridge -= cube_number
        print(f'{self.name} кушает')
        # return self.satiety, house.fridge

    def to_work(self, cube_number):
        self.satiety -= cube_number
        house.money += cube_number
        print(f'{self.name} работает')

    def to_play(self, cube_number):
        self.satiety -= cube_number
        print(f'{self.name} играет')

    def buy_food(self, cube_number):
        house.fridge += cube_number
        house.money -= cube_number
        print(f'{self.name} покупает продукты')


# MAIN CODE=======================================================================  
person = Human('Artem', 19)
house = House()
person.year()



# AttributeError: 'Human' object has no attribute 'fridge'
# AttributeError: type object 'Human' has no attribute 'satiety'

# я не могу понять...у Human есть self.satiety = satiety, в основном коде
# я передаю person = Human('Artem', 19)
# а тут (f'сытость: {Human.satiety:<10}') мне выдает что у Human нет 'satiety'