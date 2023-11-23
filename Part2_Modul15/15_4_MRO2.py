# Задача 2. Фигуры
# При моделировании компьютерных объектов используются два типа фигур: 
# прямоугольники и квадраты. Каждая из них имеет координаты XY, длину и ширину. 
# Также каждая фигура может менять координаты (двигаться) и менять размер. 

# Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и 
# квадрат — это разные фигуры и работают они по-разному. В частности, по разному 
# работает метод изменения размера фигуры, так как у квадрата все стороны равны.

from abc import ABC, abstractmethod

class Figure(ABC):
    """
        Абстрактный базовый класс Фигура
        Args и Attrs:
            x(int): координата X
            y(int): координата Y
            lenght(int): длина фигуры
            width(int): ширина фигуры
    """
    def __init__(self, x: int, y: int, lenght: int, width: int) -> None:
        self.x = x
        self.y = y
        self.lenght = lenght
        self.width = width

    @abstractmethod    
    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # def resize(self, lenght: int, width: int) -> None:
    #     self.lenght = lenght
    #     self.width = width


class ResizeMixin:
    def resize(self, lenght: int, width: int) -> None:
        self.lenght = lenght
        self.width = width


class Rectangle(Figure, ResizeMixin):
    """ Прямоугольник - родительский класс: Figure"""
    pass