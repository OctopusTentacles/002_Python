# Задача 3. Собачьи бега
#
# В собачьих бегах участвует N собак, у каждой из них 
# есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки. 
# Однако при выводе был обнаружен баг:
# собаки с наибольшим и наименьшим количеством очков 
# поменялись местами! Нужно это исправить.
#
# Дан список очков из N собак. Напишите программу, 
# которая меняет местами наибольший и наименьший элементы в списке.

points = []

N = int(input('Кол-во собак: '))
for dog in range(1, N + 1):
    print(f'У собаки {dog} очков:', end = ' ')
    point = int(input())
    points.append(point)

if list:
    maximum = points[0]
    minimum = points[0]
    maximum_index = 0
    minimum_index = 0

    for index, i in enumerate(points):
        if maximum < i:
            maximum = i
            maximum_index = index
        if minimum > i:
            minimum = 1
            minimum_index = index


else:
    print('В списке нет чисел')