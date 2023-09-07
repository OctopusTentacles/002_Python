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
    def __init__(self, index):
        self.index = index
        self.name = 'Воин_' + str(index)
        self.health = 100

    def print_status(self):
        print(f'{self.name} здоровье: {self.health}')






class Fight:
    def __init__(self, count):
        self.warriors = [Warrior(index) for index in range(1, count + 1)]

        for warrior in self.warriors:
            warrior.print_status()









    def hit(self, target):
        if self.health > 0:
            self.health -= 20
            print(f'{target} атаковал!')
        else:
            print('нет здоровья')
      
         


        
tour = Fight(2)