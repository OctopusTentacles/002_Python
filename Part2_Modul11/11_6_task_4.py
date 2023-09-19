# Задача 04. Магия
# Что нужно сделать
# Для одной игры необходимо реализовать механику магии, где при соединении двух 
# элементов получается новый. У нас есть четыре базовых элемента: 
# «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые: 
# «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

# Вот таблица преобразований:

# Вода + Воздух = Шторм
# Вода + Огонь = Пар
# Вода + Земля = Грязь
# Воздух + Огонь = Молния
# Воздух + Земля = Пыль
# Огонь + Земля = Лава
# Напишите программу, которая реализует все эти элементы. 
# Каждый элемент необходимо организовать как отдельный класс. 
# Если результат не определён, то возвращается None.

# Примечание: сложение объектов можно реализовывать через магический метод 
# __add__, вот пример использования:

# class Example_1:
#     def __add__(self, other):
#         return Example_2()

# class Example_2:
#     answer = 'сложили два класса и вывели'

# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)
# Дополнительно: придумайте свой элемент (или элементы), а также реализуйте 
# его взаимодействие с остальными элементами.


class Water:
    name = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm.name
        elif isinstance(other, Fire):
            return Steam.name
        elif isinstance(other, Earth):
            return Dirt.name
        else:
            return None

class Air:
    name = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning.name
        elif isinstance(other, Earth):
            return Dust.name
        else:
            return None

class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava.name
        else:
            return None

class Earth:
    name = 'Земля'

class Storm:
    name = 'Шторм'

class Steam:
    name = 'Пар'

class Dirt:
    name = 'Грязь'

class Lightning:
    name = 'Молния'

class Dust:
    name = 'Пыль'

class Lava:
    name = 'Лава'


# MAIN CODE=========================================================================
water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(f'Вода + Воздух = {water + air}')
print(f'Вода + Огонь = {water + fire}')
print(f'Вода + Земля = {water + earth}')

print(f'Воздух + Огонь = {air + fire}')
print(f'Воздух + Земля = {air + earth}')
print(f'Воздух + Вода = {air + water}')

print(f'Огонь + Земля = {fire + earth}')
print(f'Огонь + Воздух = {fire + air}')
print(f'Огонь + Вода = {fire + water}')
