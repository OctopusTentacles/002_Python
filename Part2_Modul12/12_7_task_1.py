# Задача 01. Налоги
# Что нужно сделать
# Реализуйте иерархию классов, описывающих имущество налогоплательщиков. 
# Она должна состоять из базового класса Property и производных от него классов 
# Apartment, Car и CountryHouse.

# Базовый класс должен иметь атрибут worth (стоимость), 
# который передаётся в конструктор, и метод расчёта налога, переопределённый 
# в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 
# её стоимости, на машину — 1/200, на дачу — 1/500.

# Каждый дочерний класс должен иметь конструктор с одним параметром, 
# передающий свой параметр конструктору базового класса.

# Разработайте интерфейс программы. Пусть она запрашивает у пользователя 
# количество его денег и стоимость имущества, а затем выдаёт налог на 
# соответствующее имущество и показывает, сколько денег ему не хватает (если это так).


class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_calc(self):
        pass

    
class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        return self.worth / 500
