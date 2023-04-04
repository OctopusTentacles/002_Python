print('Задача 6. НОД')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))


if num_1 > num_2:
    point = num_2
else:
    point = num_1

for i in range(1, point + 1):
    if (num_1 % i == 0) and (num_2 % i == 0):
        print('наибольший общий делитель', i)
