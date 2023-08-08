# Задача 5. Список списков — 2
# Что нужно сделать
# Вы уже работали с многомерными списками и решали задачи, 
# где с помощью list comprehensions «выпрямляли» многомерные списки в один. 
# Это не получится, если списков неограниченное количество 
# и у элементов разные уровни вложенности.
# Дан такой список:
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], 
#              [[11, 12, 13], [14, 15], [16, 17, 18]]]
# Напишите рекурсивную функцию, которая раскрывает все вложенные списки, 
# то есть оставляет только внешний список. 

# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# Функция должна получать список и возвращать его раскрытую версию 
# (не нужно добавлять элементы в список, записанный в глобальную переменную, 
# созданную снаружи функции).

# Подсказка
# Можно возвращать списки и срезы списков.


def expand_list(data):

    if data == []:
        return data
    if isinstance(data[0], list):
        return (expand_list(data[0]) + expand_list(data[1:]))
    return data[0] + expand_list(data[1:])

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], 
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(expand_list(nice_list))