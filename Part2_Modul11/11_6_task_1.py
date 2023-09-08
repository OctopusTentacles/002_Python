# Задача 1. Драка
# Что нужно сделать
# Вы работаете в команде разработчиков мобильной игры, 
# и вам досталась часть от ТЗ заказчика.

# Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье 
# в 100 очков. Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье 
# не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После 
# каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника 
# осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, 
# программа завершается сообщением о том, кто одержал победу.

# Реализуйте такую программу.


import random


class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def print_info(self):
        print(f'У {self.name} здоровье: {self.health}')


warrior_1 = Warrior('Воин_1', 100)
warrior_2 = Warrior('Воин_2', 100)

while warrior_1.health > 0 and warrior_2.health > 0:

    if random.randint(1, 2) == 1:
        print(f'Атакует {warrior_1.name}')
        warrior_2.health -= 20
    else:
        print(f'Атакует {warrior_2.name}')
        warrior_1.health -= 20

    warrior_1.print_info()
    warrior_2.print_info()


if warrior_1.health <= 0:
    print(f'Победил {warrior_2.name}')
else:
    print(f'Победил {warrior_1.name}')
