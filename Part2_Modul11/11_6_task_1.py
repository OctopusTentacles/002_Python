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
    def __init__(self, name, health=100):
        self.name = name
        self.health = health


    def print_status(self):
        print(warrior_1, warrior_2)



    def hit(self, target):
        if self.health > 0:
            self.health -= 20
            print(f'{target} атаковал!')
        else:
            print('нет здоровья')
        print_status()
         


    def fight(self):
        if random.randint(1,2) == 1:
            warrior_1.hit(warrior_2)
            print(f'{warrior_1.name} бьет {warrior_2.name}')
        else:
            warrior_2.hit(warrior_1)
            print(f'{warrior_2.name} бьет {warrior_1.name}')




warrior_1 = Warrior('Воин_1')
warrior_2 = Warrior('Воин_2')

fight()