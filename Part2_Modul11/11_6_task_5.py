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
    def __init__(self, person):
        self.fridge = 50
        self.money = 0
        self.person = person

    def info(self):
        print(f'\033[0;33mеды: {self.fridge:<10}'
              f'денег: {self.money:<10}'
              f'сытость: {person_1.satiety:<10}\033[0m')


class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        
    def life_year(self):
        for day in range(1, 366):
            print(f'\n\033[1;32mДень {day}:\033[0m')
            house.info()

            cube_number = random.randint(1, 6)
            print('Генерируется число кубика:', cube_number,)
            
            if self.satiety < 0:
                print(f'\033[1;31m{self.name} умирает.')
                break

            elif self.satiety < 20:
                print(f'Нужно поесть!', end=' ')
                self.to_eat(cube_number)
            elif house.fridge < 10:
                print(f'Еда кончается! Идем в магазин,', end=' ')
                self.buy_food(cube_number)
            elif house.money < 50:
                print(f'Мало денег! Идем работать!', end=' ')
                self.to_work(cube_number)
            elif cube_number == 1:
                print(f'Нужно работать!', end=' ')
                self.to_work(cube_number)
            elif cube_number == 2:
                print(f'Охото поесть!', end=' ')
                self.to_eat(cube_number)

            else:
                print(f'Время расслабиться!', end=' ')
                self.to_play(cube_number)

                
    def to_eat(self, cube_number):
        if house.fridge < cube_number or house.fridge == 0:
            print(f'Недостаточно продуктов, надо идти в магазиин!')
            self.buy_food(cube_number)
        else:    
            self.satiety += cube_number
            house.fridge -= cube_number
            print(f'{self.name} кушает')

    def to_work(self, cube_number):
        self.satiety -= cube_number
        house.money += cube_number
        print(f'{self.name} работает')

    def to_play(self, cube_number):
        self.satiety -= cube_number
        print(f'{self.name} играет')

    def buy_food(self, cube_number):
        if house.money < cube_number or house.money == 0:
            print(f'Недостаточно денег, надо идти работать!')
            self.to_work(cube_number)
        else:
            house.fridge += cube_number
            house.money -= cube_number
            print(f'{self.name} покупает продукты')


# MAIN CODE=======================================================================  
person_1 = Human('Вася')
person_2 = Human('Маша')

house = House(person_1)
house = House(person_2)

person_1.life_year()



# AttributeError: 'Human' object has no attribute 'fridge'
# AttributeError: type object 'Human' has no attribute 'satiety'

# я не могу понять...у Human есть self.satiety = satiety, в основном коде
# я передаю person = Human('Artem', 19)
# а тут (f'сытость: {Human.satiety:<10}') мне выдает что у Human нет 'satiety'
# спустя время: добавил в класс House - self.person = person
#               и в основном передал house = House(person) - вроде сработало
#               это получается вроде какой-то связи между классами?

# вот с такими моментами я не разобрался - PROBLEM )))))