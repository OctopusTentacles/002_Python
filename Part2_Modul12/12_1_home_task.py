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
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()


class Fire:
    def __str__(self):
        return 'Огонь'


class Earth:
    # TODO дописать класс
    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return 'Шторм'
        




water = Water()
air = Air()


print(f'Вода + Воздух = {water + air}')
