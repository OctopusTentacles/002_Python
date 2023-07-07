# Задача 08. Снова палиндром

# Пользователь вводит строку. Необходимо написать программу, которая определяет, 
# существует ли у этой строки такая перестановка, при которой она станет палиндромом. 
# Выведите соответствующее сообщение.

# Пример 1:
# Введите строку: aab
# Можно сделать палиндромом
# Пример 2:

# Введите строку: aabc
# Нельзя сделать палиндромом

# Основной функционал описан в отдельной функции(-ях)


def shifting(shift_text):
    shift_text = shift_text[1:] + shift_text[0]
    palindron(shift_text)


def palindron(text):
    for index in range(len(text)//2):
        if text[index] != text[-1 - index]:
            print(text[index], text[-1 - index])
            shifting(text)
    else:
        return True
        

word = (input('Введите слово: '))
if palindron(word):
    print('Можно сделать палиндромом')
print('Нельзя сделать палиндромом')


