# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. 
# Реализуйте функцию, которая эмулирует работу цикла for с помощью 
# цикла while и проходит во всем элементам итерируемого объекта. 
# Не забудьте про исключение «конца итерации».


import random

lenght = int(input("Введите длину списка: "))
my_list = [random.randint(0, 20) for _ in range(lenght)]

buffer = iter(my_list)

while True:
    try:
        print(next(buffer))
    except StopIteration:
        print("Конец итерации!")
        break