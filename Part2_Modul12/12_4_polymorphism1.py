# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). 
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).

# Также есть два дочерних класса:
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению. 
# Реализуйте родительский и дочерние классы и их методы, 
# используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).


class Unit:
    def __init__(self, hitpoint=100):
        self.hitpoint = hitpoint

    def __str__(self):
        return f"У {self.__class__.__name__} осталось здоровья {self.hitpoint}"

    def damage(self, damage=0):
        self.damage = damage
        self.hitpoint -= self.damage


class Soldier(Unit):
    def __init__(self, hitpoint):
        super().__init__(hitpoint)

    def damage(self, damage):
        super().damage(damage)

    def __str__(self):
        info = super().__str__()
        return f"получаемый урон {self.damage}\n{info}"



class Citizen(Unit):
    pass


soldier = Soldier(hitpoint=120)
soldier.damage(damage=50)
print(soldier)