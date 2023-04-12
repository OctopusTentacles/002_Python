# Задача 2. Тестирование

# Команде программистов отдали на тестирование новую модель суперкомпьютера.
# Для начала программисты решили проверить, как у компьютера обстоят
# дела с вычислениями вещественных чисел.
# Разработчики компьютера предупредили, что на входе он
# работает только с экспоненциальной формой числа.

# Пользователь вводит число N в экспоненциальной форме,
# где мантисса всегда равна числу от 1 до 9, а порядок меньше нуля.
# Также есть переменная Х, которая изначально равна единице.
# Посчитайте, сколько раз нужно прибавить N к Х, чтобы оно перевалило за двойку.

# Дополнительно: обеспечьте контроль ввода.

# Пример 1:
# Введите число в эксп. форме: 1e-3
# Кол-во прибавлений: 1001

# Пример 2:
# Введите число в эксп. форме: 5.02e-1
# Кол-во прибавлений: 2


# def input_check(n):
#     while True:
#         if abs(n + 1e-15) > 0.9:
#             print('Неверный ввод')
#             n = float(input('Введите число в эксп. форме: '))
#         else:
#             break


# x = 1
# n = float(input('Введите число в эксп. форме: '))
# input_check(n)

# n = float(n)
# count = 0
# while x <= 2:
#     x += n
#     count += 1

# print('Кол-во прибавлений:', count)


def input_check(n):
    mantissa = ''
    order = False
    for i in n:

        if order:
            if i == '-':
                print('Порядок отрицательный')      # для проверки
                return True
            else:
                print('Порядок не соответствует условию!')

        if i == 'e':
            if float(mantissa) >= 1 and float(mantissa) <= 9:
                print('мантисса =', (mantissa))     # для проверки
                order = True
            else:
                print('Мантисса не соответствует условию!')
        
        else:
            mantissa += i


x = 1
while True:
    n = (input('\nВведите число в эксп. форме: '))
    if input_check(n):
        break

n = float(n)
count = 0
while x <= 2:
    x += n
    count += 1

print('Кол-во прибавлений:', count)
