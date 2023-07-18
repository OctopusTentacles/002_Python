# В Python встроена реализация хеш-функции — hash. 

tuple = (1, 2, 3) # Есть неизменяемый объект (кстати, попробуйте потом повторить этот код с изменяемым объектом)
hash_value = hash(tuple) # Применим к этому объекту функцию hash
print(hash_value) # Проверим, что получилось (бессмысленный набор чисел)

hash_value_2 = hash(tuple) # Попробуем ещё раз
print(hash_value_2) # Опять набор чисел
print(hash_value == hash_value_2) # И он в точности равен первому


# Хеш-таблица 
tuple = (1, 2, 3) # Возьмём тот же кортеж
print(hash(tuple)) # Его хеш при каждом запуске может отличаться
# При моём запуске хеш был равен числу 529344067295497451
hash_dict = {(1, 2, 3): 'hello'} # Если я захочу создать словарь с этим кортежем,
# то «под капотом» будет создан массив, в котором по индексу 529344067295497451 
# будет храниться пара (1, 2, 3) и 'hello'


# Алгоритм Рабина — Карпа

def rabin_karp_search(text, pattern):
    # Проверяем случаи, когда текст или подстрока пустые
    if not text or not pattern:
        return []

    # Вычисляем хеш-значение для подстроки и первого окна текста
    pattern_hash = hash(pattern)
    window_hash = hash(text[:len(pattern)])

    matches = [] # Список индексов совпадений

    # Проходим по тексту с помощью скользящего окна
    for i in range(len(text) - len(pattern) + 1):
        # Если хеш-значения совпадают, сравниваем каждый символ окна с подстрокой
        if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
            # Стоит уточнить, что благодаря ленивому выполнению Python, если первое условие в связке AND вернёт False, то второе не будет запускаться вообще
            matches.append(i)

        # Обновляем хеш-значение для следующего окна
        window_hash = hash(text[i + 1:i + len(pattern) + 1])

    return matches

# Пример использования
text = "abracadabra"
pattern = "cad"
matches = rabin_karp_search(text, pattern)
print(f"Совпадения найдены на позициях: {matches}")
