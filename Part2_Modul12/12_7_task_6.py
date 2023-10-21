# Задача 06. Абстрактный класс
# Контекст
# Вы работаете в компании, занимающейся разработкой программного обеспечения для 
# архитектурных проектов. Вам необходимо разработать программу для расчёта 
# площади различных геометрических фигур, таких как круги, прямоугольники и треугольники.

# Задача
# Создайте:
# класс Shape, который будет базовым классом для всех фигур и будет хранить 
# пустой метод area, который наследники должны переопределить;
# класс Circle;
# класс Rectangle;
# класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape 
# и реализуют метод для вычисления площади фигуры.

# Дополнительно: изучите информацию о работе с абстрактными классами. 
# https://docs-python.ru/tutorial/klassy-jazyke-python/abstraktnye-klassy/

# На основе этой информации сделайте так, чтобы:
# Нельзя было создавать объекты класса Shape.
# Наследники класса Shape переопределяли его метод area, 
# чтобы объекты этих классов можно было использовать.


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return round(math.pi * self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return round(self.side_a * self.side_b)


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return round((self.side * self.height) / 2)


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# # Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# # Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
