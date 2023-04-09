# 13.5 Алгоритмы с заданной точностью

import math

precision = float(input('Точность: '))
result = 0
i = 0
addMember = 1
while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1

print('Результат', result)
print('Константа', math.e)
