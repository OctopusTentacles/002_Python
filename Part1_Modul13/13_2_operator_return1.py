# Задача 1. Сумма чисел 2

# Пользователь вводит число N. Напишите функцию summa_n,
# которая принимает одно целое положительное число N и находит
# сумму всех чисел от 1 до N включительно. Функция вызывается два раза:
# сначала от числа N, а затем от полученной суммы.

# Пример работы программы:
# Введите число: 5
# Сумма от 1 до 5 = 15
# Сумма от 1 до 15 = 120

def summa_n(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


number = int(input('Введите число: '))

fun1 = summa_n(number)
print(f'Сумма от 1 до {number} = {fun1}')

fun2 = summa_n(fun1)
print(f'Сумма от 1 до {fun1} = {fun2}')