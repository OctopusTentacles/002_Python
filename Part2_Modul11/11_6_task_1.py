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

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def 



warrior_1 = Warrior('Воин_1')
warrior_2 = Warrior('Воин_2')

