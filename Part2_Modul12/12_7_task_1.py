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

    def tax_calc(self, tax):
        print(f"Налог на {self.__class__.__name__} = {tax}")
        if self.worth > tax:
            self.worth -= tax
            print(f"Ваш баланс: {self.worth}")
        else:
            print(f"Недостаточно средств!")

    # def __str__(self):
    #     return f"Стоимость {self.__class__.__name__} {self.worth}"

    
class Apartment(Property):    
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        super().tax_calc(self.worth / 1000)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        super().tax_calc(self.worth / 200)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        super().tax_calc(self.worth / 500)


"""MAIN CODE"""
money = int(input("Сколько у вас денег? "))
apartment = Apartment(int(input(f"цена квартиры: ")))
car = Car(int(input("цена машины: ")))
house = CountryHouse(int(input("цена дачи: ")))

# print(apartment)
apartment.tax_calc()
car.tax_calc()
house.tax_calc()