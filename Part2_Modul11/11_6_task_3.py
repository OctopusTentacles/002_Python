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
        self.kids = {}
        
    def parent_info(self):
        self.name = input('Как вас зовут: ')
        self.age = int(input('сколько вам лет: '))

        child = Child('', 0)
        child.child_info()
        print(f'\nМеня зовут {self.name}, мой возраст {self.age} '
              f'и у меня есть {len(self.kids)} детей.')
        for name, age in self.kids.items():
            print(f'Ребенок {name:<7} Возраст: {age} ')
        child.child_status()

    def parent_feed(self, name):
        print(f'{self.name} торопится накормить {name}')

    def parent_action(self, name):
        print(f'{self.name} успокаивает {name}')

    def parent_rest(self):
        print(f'{self.name} спит')


        
        


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cry = {0: 'спокоен', 1: 'кричит'}
        self.hungry = {0: 'сытый', 1: 'голодный'}

    def child_info(self):
        count_kids = int(input('\nСколько детей? '))

        for _ in range(count_kids):
            self.name = (input('Имя ребенка: '))
            while True:
                try:
                    self.age = int(input('Возраст ребенка: '))
                    if parent.age - self.age < 16:
                        raise Exception
                    parent.kids[self.name] = self.age
                except ValueError:
                    print('\033[0;31mвведите целое число\033[0m')
                    continue
                except Exception:
                    print('\033[0;31mваш возраст и возраст ребенка '
                          'не соответствуют действительности\033[0m')
                    continue
                break

    def child_status(self):
        print('\nСейчас:')
        for name in parent.kids.keys():
            status_hugry = random.randint(0, 1)
            status_cry = random.randint(0, 1)
            print(f'Ребенок {name:<7} {self.hungry[status_hugry]} '
                    f'и {self.cry[status_cry]}')
            
            if
            if self.hungry == 1:
                parent.parent_feed(name)
            elif self.cry == 1:
                parent.parent_action(name)
            else:
                parent.parent_rest()

        

parent = Parent('', 0)
parent.parent_info()
