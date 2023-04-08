# Задача 2. Сравнение

# Так как в Python операции с вещественными числами могут давать
# неожиданные результаты (в частности, 0.1 + 0.2 не будет в точности равняться 0.3),
# стоит задача с этим как-то справляться.

# Напишите функцию eqv, которая принимает три числа и затем сравнивает
# сумму первых двух чисел с третьим с определённой степенью точности:
# до 15-го знака после точки. Если равенство выполняется, то функция
# возвращает True, иначе возвращает False.

# Пример 1:
# Введите первое число: 1.1
# Введите второе число: 2.2
# Введите третье число: 3.3
# True

# Пример 2:
# Введите первое число: 1e-14
# Введите второе число: 1e-14
# Введите третье число: 3e-14
# False

def eqv(a, b, c):
    return (abs((a + b) - c) <= 1e-15)


num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))
print(eqv(num1, num2, num3))
