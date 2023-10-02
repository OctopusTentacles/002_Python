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
        self.x = x
        self.y = 0

    def __str__(self):
        return(self.x, self.y)