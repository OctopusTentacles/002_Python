# Задача 1. Координаты точки
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка». 
# Модернизируйте класс по следующему условию: объект «Точка» на плоскости 
# имеет координаты x и y; при создании новой точки могут передаваться 
# пользовательские значения координат, по умолчанию x = 0, y = 0. 

# Реализуйте класс, который будет представлять эту точку, 
# и напишите следующие методы:

# Предоставление информации о точке (используйте магический метод str).
# Геттер и сеттер для x.
# Геттер и сеттер для y.
# Для сеттеров реализуйте проверку на корректность входных данных: 
# координаты должны быть числом.


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'x = {}, y = {}'.format(self.__x, self.__y)
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__x = checker_value
        
    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = checker_value

    def check_value(self, value):
        if isinstance(value, str) and value.isdigit():
            value = float(value)
        if isinstance(value, (int, float)):
            return value
        return None

        
point_1 = Point(5, g)
point_2 = Point(10, 15)
print(point_1)
print(point_2)
