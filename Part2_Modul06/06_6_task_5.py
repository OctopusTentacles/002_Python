# Задание 5. Словарь синонимов

# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов. 
# На вход в программу подаётся N пар слов. 
# Каждое слово является синонимом для своего парного слова. 

# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), 
# затем запрашивает у пользователя слово и выводит на экран его синоним. 
# Обеспечьте контроль ввода: если такого слова нет, выведите ошибку 
# и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.

# Пример
# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет


amount = int(input('Введите количество пар слов: '))
for 