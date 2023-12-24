# Напишите функцию is_palindrome(s), которая принимает строку s и возвращает True, 
# если строка является палиндромом, и False в противном случае. Палиндром - 
# это строка, которая читается одинаково слева направо и справа налево, 
# игнорируя пробелы, знаки препинания и регистр.

# Примеры:


import re
from collections import Counter


def is_palindrome(text: str) -> bool:
    
    # Большие буквы преобразуем в маленькие:
    low_text = text.lower()
    # убираем пробелы и все спецсимволы:
    new_text = re.sub(r"[^aA-zZ]", "", low_text)

    # считаем кол-во каждого элемента:
    char_count = Counter(new_text)

    # считаем кол-во нечетных - их должно быть не больше 1
    odd_count = sum(map(lambda value: value % 2 !=0, char_count.values()))

    # если нечетных не больше 1 - True:
    return odd_count <= 1



print(is_palindrome("radar"))  # True
print(is_palindrome("A man, a plan a canal Panama!"))  # True
print(is_palindrome("hello"))  # False