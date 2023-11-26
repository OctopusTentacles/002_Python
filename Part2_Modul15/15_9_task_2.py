# Задача 2. Математический модуль
# Вася использует в своей программе очень много различных математических вычислений, 
# связанных с фигурами. Например, нахождение их площадей или периметров. 
# Поэтому, чтобы не захламлять код огромным количеством функций, 
# он решил выделить для них отдельный класс, подключить как модуль 
# и использовать по аналогии с модулем math.

# Реализуйте класс MyMath, состоящий как минимум из следующих методов 
# (можете бонусом добавить и другие методы):

# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.

# Результат:
# 31.41592653589793
# 113.09733552923255

import math


class MyMath:

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """ 
            Вычисляет длину окружности.
        """
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
            Вычисляет площадь окружности.
        """
        return math.pi * radius**2

    @classmethod
    def cube_volume(cls, side_length: float) -> float:
        """
            Вычисляет объем куба.
        """
        return side_length**3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        """
            Вычисляет площадь поверхности сферы.
        """
        return 4 * math.pi * radius**2
    

# Пример использования:
res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

