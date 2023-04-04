print('Задача 6. НОД')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def NOD(n1, n2):
    if n1 > n2:
        point = n2
    else:
        point = n1

    for i in range(1, point + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            nod = i
    print('Наибольший общий делитель:', nod)


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
NOD(num_1, num_2)
