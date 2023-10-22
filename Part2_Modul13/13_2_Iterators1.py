# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. 
# Реализуйте функцию, которая эмулирует работу цикла for с помощью 
# цикла while и проходит во всем элементам итерируемого объекта. 
# Не забудьте про исключение «конца итерации».


import random

amt = int(input("Введите количество чисел: "))

my_list = [random.randint(0, 10) for _ in range(amt)]
buffer_iter = iter(my_list)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration:
        print("конец итерации")
        break