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
    family = dict()
    def __init__(self, count):
        self.count = count
        
        for index in range(1, self.count + 1):
            Member.name = input(f'Введите имя жильца {index}: ')
# сытость________________________________________:
            self.family[Member.name.title()] = 50
        Member.life_year(self)

# статистика ресурсов____________________________:   
    def info(self):
        print(f'\033[0;33mеды: {House.fridge:<5}'
              f'денег: {House.money:<5}', end='')
        for member, satiety in self.family.items():
            print(f'сытость {member}: {satiety:<5}', end='')


class Member:
    name = ''
    
    def __init__(self, index):
        self.index = index
        
    def life_year(self):
        try:
            for day in range(1, 366):
                print(f'\n\033[1;32mДень {day}:\033[0m')
                Create.info(self)

                for name in Create.family:
                    cube_number = random.randint(1, 6)
                    print(f'\033[0m\nОчки действия {name}: {cube_number}')
                    
                    if Create.family[name] < 0:
                        raise Exception

                    elif Create.family[name] < 20:
                        print(f'Нужно поесть!', end=' ')
                        Member.to_eat(self, cube_number, name)
                    elif House.fridge < 10:
                        print(f'Еда кончается! Идем в магазин!', end=' ')
                        Member.buy_food(self, cube_number, name)
                    elif House.money < 50:
                        print(f'Мало денег! Идем работать!', end=' ')
                        Member.to_work(self, cube_number, name)
                    elif cube_number == 1:
                        print(f'Нужно работать!', end=' ')
                        Member.to_work(self, cube_number, name)
                    elif cube_number == 2:
                        print(f'Охото поесть!', end=' ')
                        Member.to_eat(self, cube_number, name)

                    else:
                        print(f'Время расслабиться!', end=' ')
                        Member.to_play(self, cube_number, name)
            print(f'\033[1;32mУдалось прожить {day} дней!')

        except Exception:
            print(f'\033[1;31m{name} умирает.')
            print('Такое проживание не допустимо!\033[0m')
            
       
    def to_eat(self, cube_number, name):
        if House.fridge < cube_number or House.fridge == 0:
            print(f'Недостаточно продуктов, надо идти в магазиин!')
            Member.buy_food(self, cube_number, name)
        else:    
            Create.family[name] += cube_number
            House.fridge -= cube_number
            print(f'{name} кушает')

    def to_work(self, cube_number, name):
        Create.family[name] -= cube_number
        House.money += cube_number
        print(f'{name} работает')

    def to_play(self, cube_number, name):
        Create.family[name] -= cube_number
        print(f'{name} играет')

    def buy_food(self, cube_number, name):
        if House.money < cube_number or House.money == 0:
            print(f'Недостаточно денег, надо идти работать!')
            Member.to_work(self, cube_number, name)
        else:
            House.fridge += cube_number
            House.money -= cube_number
            print(f'{name} покупает продукты')


# MAIN CODE=======================================================================  
num = int(input('Сколько человек будут жить вместе?: '))
family = Create(num)


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