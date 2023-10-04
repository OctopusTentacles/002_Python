# Задача 1. Корабли
# Даны два класса кораблей — грузовой и военный. 
# У каждого из этих кораблей есть своя модель, и каждый может сделать два действия: 
# сообщить свою модель и идти по воде. 

# Грузовой корабль имеет такой атрибут, как заполненность, 
# изначально он равен нулю. У него есть ещё два действия: 
# погрузить и выгрузить груз с корабля. 

# У военного же корабля нет никаких грузов, есть только оружие, 
# которое передаётся вместе с моделью. Также, вместо погрузки и выгрузки, 
# у него есть другое действие — атаковать.

# Реализуйте классы грузового и военного кораблей. Для этого выделите общие 
# атрибуты и методы в отдельный класс «Корабль» и используйте наследование. 
# Не забудьте про функцию super в дочерних классах.


class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f"Ship's model is {self.__model}"
    
    def sail(self):
        print("Ship is swiming!")


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.fullness = 0

    def load(self):
        print("Ship is loading")

    def unload(self):
        print("Ship is inloading")



class BattleShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print("Корабль атакует оружием", self.gun)