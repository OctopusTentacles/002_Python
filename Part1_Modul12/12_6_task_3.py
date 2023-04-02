print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел,
# но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить
# функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр,
# максимальную или минимальную цифру.

# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы,
# максимума и минимума при помощи аргументов.


def menu():
    print('Что сделать с числом?')
    print('1 = вывести сумму его цифр')
    print('2 = вывести максимальную цифру')
    print('3 = вывести минимальную цифру')
    action = int(input('Введите номер действия: '))
    if action == 1:
        digits_sum(number)
    elif action == 2:
        digits_max(number)
    elif action == 3:
        digits_min(number)
    else:
        print('Ошибка, повторите ввод!')
        menu()


def digits_sum(n):
    summa = 0
    while n > 0:
        digit = n % 10
        summa += digit
        n //= 10
    print('Сумма цифр числа равна:', summa)


def digits_max(n):
    maxDigit = 0
    while n > 0:
        digit = n % 10
        if digit > maxDigit:
            maxDigit = digit
        n //= 10
    print('Максимальная цифра числа равна:', maxDigit)


def digits_min(n):
    minDigit = n
    while n > 0:
        digit = n % 10
        if digit < minDigit:
            minDigit = digit
        n //= 10
    print('Минимальная цифра числа равна:', minDigit)


number = int(input('Введите чило: '))
menu()
