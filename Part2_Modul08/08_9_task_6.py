# Задача 6. Быстрая сортировка
# Что нужно сделать
# Реализуйте алгоритм быстрой сортировки (её называют сортировкой Хоара). 

# За один шаг алгоритма выполните следующие действия:

# Выберите один элемент списка (его иногда называют опорным элементом). 
# Сделать это можно разными способами, но важно придерживаться одного принципа. 
# В нашем случае опорным элементом всегда будет крайний правый 
# (например, в списке [1, 2, 3] это 3).

# Разбейте текущий список на три части: элементы меньше опорного, 
# равные опорному и больше опорного. 
# В списке [5, 8, 9, 4, 2, 9, 1, 8] опорным элементом будет число 8 (крайнее правое), 
# а получить надо три списка:
# [5, 4, 2, 1];
# [8, 8];
# [9, 9].

# Для списка с элементами меньше опорного ([5, 4, 2, 1]) и списка 
# с элементами больше опорного ([9, 9]) 
# выполните те же шаги заново — запустите рекурсию.
# результат_1 = рекурсия([5, 4, 2, 1]).
# результат_2 = [8, 8].
# результат_3 = рекурсия([9, 9]).

# Сложите результаты вызова рекурсий и получите отсортированный список:
# отсортированный_список = результат_1 + результат_2 + результат_3.


def quick_sort(data):
    if not data:
        return data
    
    main_elem = data[-1:]
        

    low_main = [elem for elem in data if elem < main_elem[0]]
    equal_main = [elem for elem in data if elem == main_elem[0]]
    high_main = [elem for elem in data if elem > main_elem[0]]
    
    return quick_sort(low_main) + equal_main + quick_sort(high_main)


my_list = [5, 8, 9, 4, 2, 9, 1, 8]

print(quick_sort(my_list))


# 