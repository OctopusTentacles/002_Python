# Задача 3. Палиндром: возвращение

# Используя модуль collections, реализуйте функцию can_be_poly, 
# которая принимает на вход строку и проверяет, можно ли получить из неё палиндром. 


from collections import Counter


def can_be_poly(message: str) -> bool:

    return list(filter(lambda x: x % 2, Counter(message).values()))



# Пример кода:
print(can_be_poly('abcba')) #True
print(can_be_poly('abbbc')) #False

