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
    """ Базовый класс - имущество налогоплательщиков.
        имеет атрибут worth (стоимость), который передаётся в конструктор, 
        и метод расчёта налога - tax_calc
    """
    def __init__(self, worth):
        self.worth = worth

    def tax_calc(self):
        """метод расчёта налога переопределяется в каждом из производных классов
        """
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


"""MAIN CODE"""
property = {}
money = int(input("Сколько у вас денег? "))

print("\nСтоимость имущества:")

# apartment = Apartment(int(input("квартира: ")))
# apartment_tax = apartment.tax_calc()
# print(f"Налог на квартиру: {apartment_tax}")
# money -= apartment_tax
# print(f"Ваш баланс: {money}")

# car = Car(int(input("машина: ")))
# car_tax = car.tax_calc()
# print(f"Налог на машину: {car_tax}")
# money -= car_tax
# print(f"Ваш баланс: {money}")

# house = CountryHouse(int(input("дача: ")))
# house_tax = house.tax_calc()
# print(f"Налог на дом: {house_tax}")
# money -= house_tax
# print(f"Ваш баланс: {money}")

apartment = Apartment(int(input("Apartment: ")))
property[apartment.__class__.__name__] = apartment.tax_calc()

car = Car(int(input("Car: ")))
property[car.__class__.__name__] = car.tax_calc()

house = CountryHouse(int(input("CountryHouse: ")))
property[house.__class__.__name__] = house.tax_calc()

print("\nНалог на имущество:")
for key, value in property.items():
    print(f"{key}: {value}")
    money -= value

if money < 0:
    print(f"\nДля оплаты Вам не хватает: {abs(money)}")
else:
    print(f"\nОплата произведена. Ваш баланс: {money}")
