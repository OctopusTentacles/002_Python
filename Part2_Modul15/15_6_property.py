# Задача 1. Транспорт 2
# Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс 
# геттерами и сеттерами для соответствующих атрибутов. Используйте встроенные декораторы. 
# Вот входные данные той задачи:

# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, 
# и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:

# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.


from abc import ABC, abstractmethod


class Transport(ABC):
    """ 
        Абстрактный базовый класс Парк Транспорта.
    """
    def __init__(self, color, speed, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @abstractmethod
    def earth_moving(self):
        pass

    @abstractmethod
    def water_moving(self):
        pass

    def signal(self):
        print("Сигнал")


class MusicMixin:
    def play_music(self):
        print("Playing music!")


class Cars(Transport):
    def __init__(self, color, speed) -> None:
        super().__init__(color=color, speed=speed)

    def earth_moving(self):
        print("Машина едет по земле!")

class Boats(Transport):
    def __init__(self, color, speed) -> None:
        super().__init__(color=color, speed=speed)

    def water_moving(self):
        print("Лодка плывет по воде!")

class Amphibians(Cars, Boats, MusicMixin):
    pass
