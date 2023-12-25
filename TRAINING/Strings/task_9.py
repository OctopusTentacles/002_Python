# Напишите функцию is_palindrome(s), которая принимает строку s и возвращает True, 
# если строка является палиндромом, и False в противном случае. Палиндром - 
# это строка, которая читается одинаково слева направо и справа налево, 
# игнорируя пробелы, знаки препинания и регистр.


import re
from collections import Counter

def is_palindrome(text: str) -> bool:
    if not text:
        return False
    
    # Преобразование к нижнему регистру и удаление пробелов и спецсимволов:
    cleaned_text = re.sub(r"[^a-zA-Zа-яА-Я]", "", text.lower())
    # кол-во каждого символа:
    char_count = Counter(cleaned_text)
    # считаем сколько нечетных:
    odd_count = sum(i % 2 != 0 for i in char_count.values())
    # если нечетных не больше одного - True:
    return odd_count <= 1


# Тестирование
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Привет, друг! Да, туда где ты!" ))  # True
print(is_palindrome("Hello, World!"))  # False
print(is_palindrome(""))  # False