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

def sorting(my_list):
    max_index = my_list[size - 1]
    for i in range(len(my_list)):
        for index in my_list:
            if index > max_index:
                num_list.append(index)

num_list = []

size = int(input('Укажите размер списка: '))

fill_list(size)
print('Изначальный список:', num_list)

sorting(num_list)
print('Отсортированный список:', num_list)