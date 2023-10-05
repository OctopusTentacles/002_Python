# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). 
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).

# Также есть два дочерних класса:
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению. 
# Реализуйте родительский и дочерние классы и их методы, 
# используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).


class Unit:
    def __init__(self, hitpoint):
        self.__hitpoint = hitpoint

    def __str__(self):
        return f"У {self.__class__.__name__} осталось здоровье {self.__hitpoint}"

    def set_hitpoint(self, hitpoint):
        if isinstance(hitpoint, int):
            self.__hitpoint = hitpoint
        else:
            raise Exception("Ошибка! Надо число!")

    def get_hitpoint(self):
        return "У {} здоровье {}".format(self.__class__.__name__, self.__hitpoint)

    def damage(self, damage=0):
        self.damage = damage
        self.__hitpoint -= self.damage

        
class Soldier(Unit):

    def damage(self, damage):
        super().damage(damage)

    def __str__(self):
        info = super().__str__()
        return f"получаемый урон {self.damage}\n{info}"


class Citizen(Unit):

    def damage(self, damage):
        
        self.damage = damage * 2
        super().damage(self.damage)

    def __str__(self):
        info = super().__str__()
        return f"получаемый урон {self.damage}\n{info}"


soldier = Soldier(hitpoint=120)
print(soldier.get_hitpoint())
soldier.damage(damage=50)
print(soldier)

citizen = Citizen(hitpoint=100)
print(citizen.get_hitpoint())
citizen.damage(damage=40)
print(citizen)