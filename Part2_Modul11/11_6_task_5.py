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
        fridge = 50
        money = 0


class Create:
    family = []
    def __init__(self, count):
        self.count = count
        
        for index in range(1, self.count + 1):
            Member.name = input(f'Введите имя жильца {index}: ')
            self.family.append(Member.name.title())
        Member.life_year(self)
      
    def info(self):
        print(f'\033[0;33mеды: {House.fridge:<10}'
              f'денег: {House.money:<10}', end='')
        for member in self.family:
            print(f'сытость {member}: {Member.satiety:<5}', end='')



class Member:
    name = ''
    satiety = 50
    
    
    def __init__(self, index):
        self.index = index
        # self.name = ''
        # self.satiety = 50
        
    def life_year(self):
        for day in range(1, 36):
            print(f'\n\033[1;32mДень {day}:\033[0m')
            Create.info(self)

            for name in Create.family:

                cube_number = random.randint(1, 6)
                print(f'\033[0m\nОчки действия {name}: {cube_number}')
                
                if Member.satiety < 0:
                    print(f'\033[1;31m{name} умирает.')
                    break

                elif Member.satiety < 20:
                    print(f'Нужно поесть, {name}!', end=' ')
                    Member.to_eat(cube_number)
                elif House.fridge < 10:
                    print(f'Еда кончается, {name}! Идем в магазин,', end=' ')
                    Member.buy_food(cube_number)
                elif House.money < 50:
                    print(f'Мало денег, {name}! Идем работать!', end=' ')
                    Member.to_work(self, cube_number)
                elif cube_number == 1:
                    print(f'Нужно работать, {name}!', end=' ')
                    Member.to_work(self, cube_number)
                elif cube_number == 2:
                    print(f'Охото поесть, {name}!', end=' ')
                    Member.to_eat(cube_number)

                else:
                    print(f'Время расслабиться, {name}!', end=' ')
                    Member.to_play(cube_number)

                
    def to_eat(self, cube_number, ):
        if House.fridge < cube_number or House.fridge == 0:
            print(f'Недостаточно продуктов, надо идти в магазиин!')
            self.buy_food(cube_number)
        else:    
            Member.satiety += cube_number
            House.fridge -= cube_number
            print(f'{self.name} кушает')

    def to_work(self, cube_number):
        Member.satiety -= cube_number
        House.money += cube_number
        print(f'{Member.name} работает')

    def to_play(self, cube_number):
        Member.satiety -= cube_number
        print(f'{self.name} играет')

    def buy_food(self, cube_number):
        if House.money < cube_number or House.money == 0:
            print(f'Недостаточно денег, надо идти работать!')
            self.to_work(cube_number)
        else:
            House.fridge += cube_number
            House.money -= cube_number
            print(f'{self.name} покупает продукты')


# MAIN CODE=======================================================================  
family = Create(2)


# AttributeError: 'Human' object has no attribute 'fridge'
# AttributeError: type object 'Human' has no attribute 'satiety'

# я не могу понять...у Human есть self.satiety = satiety, в основном коде
# я передаю person = Human('Artem', 19)
# а тут (f'сытость: {Human.satiety:<10}') мне выдает что у Human нет 'satiety'
# спустя время: добавил в класс House - self.person = person
#               и в основном передал house = House(person) - вроде сработало
#               это получается вроде какой-то связи между классами?

# вот с такими моментами я не разобрался - PROBLEM )))))

# теперь не могу второго человека добавить