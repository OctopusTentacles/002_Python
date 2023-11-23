# Задача 1. Транспорт
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет 
# двигаться и подавать сигнал. В парке транспорта стоят:

# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен 
# быть абстрактным и содержать абстрактные методы.

# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. 
# «Замешайте» этот класс в «Амфибию»

from abc import ABC, abstractmethod

class Transport(ABC):
    """ 
        Абстрактный базовый класс Парк Транспорта.
    """
    def __init__(self, color, speed, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color
        self.speed = speed

    @abstractmethod
    def earth_moving(self):
        pass

    @abstractmethod
    def water_moving(self):
        pass


    @abstractmethod
    def beep(self):
        pass


class MusicMixin:
    def play_music(self):
        print("Playing music!")


class Cars(Transport):
    def __init__(self, color, speed) -> None:
        super().__init__(color=color, speed=speed)

    def earth_moving(self):
        super().earth_moving(self)
        print("Машина едет по земле!")

class Boats(Transport):
    def __init__(self, color, speed) -> None:
        super().__init__(color=color, speed=speed)

    def water_moving(self):
        super().water_moving(self)
        print("Лодка плывет по воде!")

class Amphibians(Transport, MusicMixin):
    def __init__(self, color, speed) -> None:
        super().__init__(color=color, speed=speed)

    def earth_moving(self):
        super().earth_moving(self)
        print("Амфибия едет по земле!")

    def water_moving(self):
        super().water_moving(self)
        print("Амфибия плывет по воде!")
