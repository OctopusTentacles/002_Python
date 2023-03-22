print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

n = int(input('Сколько чисел: '))
digit = 0
sumDigit = 0
maxDigit = 0

for i in range(1, n + 1):
    print('Введите', i, '-е число: ', end='')
    num = int(input())
    number = num
    while number > 0:
        digit = number % 10
        number //= 10
        sumDigit += digit
    if sumDigit > maxDigit:
        maxDigit = sumDigit
        maxNum = num
    sumDigit = 0
print('Число ', maxNum, 'Сумма цифр', maxDigit)
