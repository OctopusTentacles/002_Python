# Задача 2
# . Сумма и разность

# Что нужно сделать
# Напишите две функции. Первая принимает одно целое 
# положительное число N и находит сумму всех цифр в числе. 
# Вторая принимает число N и считает количество цифр в числе. 
# В ответ выводится разность суммы чисел и количества.

def sum_of_digits(num1):
    summa = 0
    while num1 > 0:
        summa += num1 % 10
        num1 //= 10
    print('Сумма цифр:', summa)
    return summa


def amt_of_digits(num2):
    count = 0
    while num2 > 0:
        count += 1
        num2 //= 10
    print('Колличество цифр:', count)
    return count


while True:
    number = int(input('Введите положительное число: '))
    if number > 0:
        break
print('Разность:', sum_of_digits(number) - amt_of_digits(number))
