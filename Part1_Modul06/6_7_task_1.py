print('Задача 1. Кубы чисел')

# В один из вечеров к Васе домой пришёл племянник и пожаловался на 
# сложности с уроками математики: у него никак не получалось 
# разобраться со степенями чисел. Вася решил помочь племяннику 
# и написать программу, которая позволит наглядно увидеть 
# возведение чисел в третью степень.

# Напишите программу, которая возводит в третью степень каждое число
# от 1 до N и выводит результат на экран.

number_N = int(input("Введите целое число: "))
number = 1
while number <= number_N:
    cube = number ** 3
    print(f"Куб числа {number} равен {cube}")
    number += 1
    