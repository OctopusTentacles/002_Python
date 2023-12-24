# Напишите функцию is_palindrome(s), которая принимает строку s и возвращает True, 
# если строка является палиндромом, и False в противном случае. Палиндром - 
# это строка, которая читается одинаково слева направо и справа налево, 
# игнорируя пробелы, знаки препинания и регистр.

# Примеры:


import re


def is_palindrome(text: str) -> bool:
    low_text = text.lower()
    new_text = re.sub(r"[^aA-zZ]", "", low_text)
    print(new_text)
    pass



print(is_palindrome("radar"))  # True
print(is_palindrome("A man, a plan a canal Panama!"))  # True
print(is_palindrome("hello"))  # False