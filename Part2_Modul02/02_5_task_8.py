# Задача 8. Сортировка

# Дан список из N чисел. Напишите программу, которая сортирует элементы списка 
# по возрастанию и выводит их на экран. Дополнительный список использовать нельзя. 
# Также нельзя использовать готовые функции sorted/min/max и метод sort.

# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

# Пример:
# Изначальный список: [1, 4, -3, 0, 10]
# Отсортированный список: [-3, 0, 1, 4, 10]


def fill_list(n):
    for i in range(n):
        num_list.append(int(input(f'Введите {i + 1} число: ')))
    return num_list


def sorting(my_list):
    for index in range(len(my_list) - 1):
        for i in range(len(my_list) - index - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


num_list = []
size = int(input('Укажите размер списка: '))

print('Изначальный список:', fill_list(size))
print('Отсортированный список:', sorting(num_list))