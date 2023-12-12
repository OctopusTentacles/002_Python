# Задача 3. Палиндром: возвращение
# Есть множество встроенных и внешних библиотек для работы с данными в Python. 
# С некоторыми из них вы уже работали. Например, с модулем collections, когда 
# использовали специальный класс OrderedDict, с помощью которого делали упорядоченный 
# словарь. В этой библиотеке есть и другие возможности, но их немного. 
# Официальная документация: collections — Container datatypes.

# Используя модуль collections, реализуйте функцию can_be_poly, 
# которая принимает на вход строку и проверяет, можно ли получить из неё палиндром. 


from collections import Counter
# Counter - коллекция, ключ - элемент, значение - кол-во элемента.
# т.е. считает колличество каждого элемента и хранит в виде словаря.
# Палиндром - все элементы должны встречаться четное кол-во раз,
# и один элемент может быть нечетным - центр.


def can_be_poly(message: str) -> bool:
    """ Функция проверки строки на палиндром;
        param message: входная строка;
        retune bool: True если можно получить палиндром и False иначе.
    """
    # кол-во каждого элемента:
    char_count = Counter(message)
    print(char_count)

    # кол-во нечетных элементов(нечетные значения в char_count)
    # odd_count = sum(1 for value in char_count.values() if value % 2 != 0 )
    odd_count = sum(map(lambda value: value % 2 != 0, char_count.values()))
    print(odd_count)

    # если кол-во нечетных символов больше одного, False
    return odd_count <= 1


# Пример кода:
print(can_be_poly('abcba')) #True
print(can_be_poly('abbbc')) #False




