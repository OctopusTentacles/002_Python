# Задача 1. Анализ цен
# Нашему другу заказали написать программу, которая анализирует цены на бирже. 
# Она получает этот пакет данных, но делать что-либо с ним нельзя. 
# Для нормальной работы аналитической программы берётся новый список, 
# который равен тому, что пришло. Затем идёт работа с новым списком: 
# если есть отрицательные цены, то программа их зануляет и в конце выводит 
# на экран, сколько денег мы по итогу потеряли. Получился вот такой код:

# original_prices = [-12, 3, 5, -2, 1]

# new_prices = original_prices

# for i in range(len(original_prices)):

#     if new_prices[i] < 0:

#         new_prices[i] = 0

# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))

# Однако при таких входных данных программа почему-то работает неправильно: 
# она выводит ответ 0, когда правильный ответ 14. Помогите другу исправить 
# программу, а также сделайте так, чтобы список цен генерировался 
# случайно (диапазон можно выбрать любой).

import random

original_prices = [random.randint(-15, 15) for _ in range(5)]
new_prices = [i if i > 0 else 0 for i in original_prices]

print('пакет данных', original_prices)
print('новый список', new_prices)
print('Мы потеряли:', abs(sum(original_prices) - sum(new_prices)))

# or

# new_prices = original_prices[::]          # копирование через срез
# for index in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print('Мы потеряли:', abs(sum(original_prices) - sum(new_prices)))