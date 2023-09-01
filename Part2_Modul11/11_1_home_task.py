# Разбор домашнего задания!
# Задача 04. Чат

import os

name = input('Как вас зовут?')

while True:
    print('Чтобы увидеть текущий текст чата введите 1,\n'
          'Чтобы написать сообщение введите 2')
    response = input('введите 1 или 2')

    if response == '1':
        try:
            with open(os.path.join(os.path.dirname(__file__), 'chat.txtx'),
                      'r', encoding='utf8') as file:
                messages = file.readlines()
                print(''.join(messages))

        except FileNotFoundError:
            print('Служебное сообщение: пока ничего нет\n')