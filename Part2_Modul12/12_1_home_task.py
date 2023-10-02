# таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

class Water:
    def __str__(self):
        return 'Вода'
    
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()

        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Fire:
    def __str__(self):
        return 'Огонь'
    
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()



class Earth:
    # TODO дописать класс
    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return 'Шторм'
        

class Vapor:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'
    

class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'

class Lava:
    def __str__(self):
        return 'Лава'



water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(f'Вода + Воздух = {water + air}')
print(f'Вода + Огонь = {water + fire}')
print(f'Вода + Земля = {water + earth}')

print(f'Воздух + Огонь = {air + fire}')
print(f'Воздух + Земля = {air + earth}')

print(f'Огонь + Земля = {fire + earth}')
