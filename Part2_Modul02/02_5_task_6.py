# Задача 6. Бегущие цифры

# Вы пишете программу для маленького табло, в котором циклически повторяется 
# один и тот же текст или числа. Например, как в метро, автобусах или трамваях.

# Даны список из N элементов и целое число K. 
# Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций. 
# Используйте минимально возможное количество операций присваивания.

# Пример 1:
# Сдвиг: 1
# Изначальный список: [1, 2, 3, 4, 5]
# Сдвинутый список: [5, 1, 2, 3, 4]

# Пример 2:
# Сдвиг: 3
# Изначальный список: [1, 4, -3, 0, 10]
# Сдвинутый список: [-3, 0, 10, 1, 4]


def fill_list(n):
    for i in range(n):
        number = int(input(f'Введите {i + 1} элемент: '))
        start_list.append(number)

start_list = []
shift_list = []

elements = int(input('Введите количество элементов списка: '))
shift = int(input('Сдвиг: '))

fill_list(elements)

print(start_list)