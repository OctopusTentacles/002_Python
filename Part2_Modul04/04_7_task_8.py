# Задание 8. Шифр Цезаря

# Юлий Цезарь использовал свой способ шифрования текста. 
# Каждая буква заменялась на следующую по алфавиту через K позиций по кругу. 
# Если взять русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать, 
# буква А станет буквой Г, Б станет Д и так далее.

# Пользователь вводит сообщение и значение сдвига. 
# Напишите программу, которая изменит фразу при помощи шифра Цезаря.

# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.


def cipher(message, shift):
    code = ''
    for symbol in range(len(message)):
        for letter in range(len(azbuka)):
            if message[symbol] == azbuka[letter]:
                code_symbol = letter + shift
                if code_symbol >= len(azbuka):
                    code_symbol -= len(azbuka)
                code += azbuka[code_symbol]
                break
        else:
            code += message[symbol]
    return code            


azbuka = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

my_message = input('Введите сообщение: ')
my_shift = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение:', cipher(my_message, my_shift))
