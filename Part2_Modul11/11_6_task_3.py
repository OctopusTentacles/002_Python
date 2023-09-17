# Задача 03. Отцы, матери и дети
# Что нужно сделать
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:

# Имя.
# Возраст.
# Список детей.
# И он может:

# Сообщить информацию о себе.
# Успокоить ребёнка.
# Покормить ребёнка.
# У ребёнка есть:

# Имя.
# Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# Состояние спокойствия.
# Состояние голода.
# Реализация состояний на ваше усмотрение. 
# Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё интереснее.


import random

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kids = []
        

    def parent_info(self):
        print(f'Меня зовут {self.name}, мой возраст {self.age} '
              f'и у меня есть {len(self.kids)} детей.')


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cry = {0: 'спокоен', 1: 'кричит'}
        self.hungry = {0: 'сытый', 1: 'голодный'}

    def child_info(self):
        count_kids = int(input('сколько детей? '))

        for i in range(count_kids):
            parent.kids.append(input('Имя ребенка: '))
            self.age = int(input('Возраст ребенка: '))
            print(f'Ребенок {self.name:<5} возраст: {self.age} ')

    def child_status(self):
        print(f'Ребенок {self.name} {self.hungry[random.randint(0, 1)]} '
              f'и {self.cry[random.randint(0, 1)]}')
        

parent = Parent('John', 35)

parent.parent_info()
child.child_info()