# Задача 1. Возможности компьютера

# В одной IT-компании тестируют возможности различных языков
# программирования, компиляторов и, конечно же, компьютеров.
# Компания дала вам задачу понять, какое самое маленькое возможное
# число можно получить путём постоянного деления числа на 2.
# Изначально число равно единице. Также, помимо самого числа,
# компания просит вывести количество делений.
# Реализуйте такую программу.

count = 0
x = 1
while x != 0:
    x /= 2
    print(x)
    count += 1

print('количество делений', count)
