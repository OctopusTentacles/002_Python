# Задача 4. Уникальный шифр
# Представьте, что вы — детектив, который получил загадочное письмо с шифровкой. 
# Нужно найти количество уникальных символов в письме, 
# чтобы разгадать его и раскрыть тайну.

# Напишите функцию, которая принимает строку и возвращает количество уникальных 
# символов в строке. Используйте для выполнения задачи lambda-функции и map и/или filter.

# Сделайте так, чтобы алгоритм НЕ был регистрозависим: 
# буквы разного регистра должны считаться одинаковыми.
# Советы:
# Работать с регистрами помогут методы строк lower/upper.
# Уникальными считаются буквы, которые повторяются только один раз 
# (например строка «аа» будет содержать 0 уникальных букв).


# from collections import Counter


def count_unique_characters(letter: str) -> int:
    """ Функция принимает строку и возвращает количество уникальных символов.
        param letter: входная строка;
        return int: кол-во уникальных символов в строке.
    """
    # low_letter = Counter(letter.lower())
    # uniq_char = sum(filter(lambda value: value == 1, low_letter.values()))

    uniq_char = list(filter(lambda sym: letter.lower().count(sym) == 1, letter.lower()))

    return len(uniq_char)


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)


# Вывод: количество уникальных символов в строке — 5.