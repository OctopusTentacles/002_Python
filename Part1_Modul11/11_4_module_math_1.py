# Задача 1. Герон

# Существует, так называемая, формула Герона, позволяющая
# вычислить площадь треугольника, зная длины его сторон.

# S= √ (p * (p - a)*(p - b)*(p - c)) ,где

# S - площадь;
# p - полупериметр треугольника (a+b+c)/2;
# a,b,c - длины сторон треугольника.

# Напишите программу, которая принимает на вход длины
# сторон треугольника и выводит его площадь

import math

a = float(input('Сторона треуголника а: '))
b = float(input('Сторона треуголника b: '))
c = float(input('Сторона треуголника c: '))

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('Площадь треугольника равна', s)