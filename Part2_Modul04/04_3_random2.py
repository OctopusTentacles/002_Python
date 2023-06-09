# Задача 2. Магазин
# У нас есть вот такой список цен на некоторые товары из магазина:

# В этом списке также хранятся цены на товары, 
# которые уже давно не продаются. По какой-то причине система, 
# вместо того чтобы их занулить, просто приписала к ним минус. 
# Нам нужно это исправить.

# Напишите программу, которая генерирует новый список из первого списка, 
# заменяя все отрицательные числа на ноль.

# Результат:
# [1.25, 0, 10.22, 3.78, 0, 1.16]


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

print([(0 if index < 0 else index) for index in original_prices])