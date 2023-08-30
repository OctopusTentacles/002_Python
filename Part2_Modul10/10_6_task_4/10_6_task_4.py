# Задача 04. Чат
# Что нужно сделать
# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, 
# то есть программа может работать одновременно для нескольких пользователей. 
# При запуске запрашивается имя пользователя. 
# После этого он выбирает одно из действий:

# 1.Посмотреть текущий текст чата.
# 2.Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.

# Примечание: для решения задачи вам будет достаточно текущих знаний, 
# нужно лишь проявить немного фантазии и хитрости. Не нужно лезть в дебри 
# работы с сетями, создания GUI-приложений и прочих штук. 
# (Но если очень хочется, то останавливать вас никто не будет!)

import os


def read_file(cur_dir):
    with open(os.path.join(cur_dir, 'chat.txt'), 
              'r', encoding='utf8') as read_chat:
        print(read_chat.readlines)



def write_file(cur_dir):
        with open(os.path.join(cur_dir, 'chat.txt'), 
              'a', encoding='utf8') as text_chat:
            # message = input('')
            text_chat.write(input('') + '\n')
            



current_directory = os.path.dirname(__file__)

while True:

    user_name = input('Введите имя пользователя: ')
    print('1. Посмотреть текущий текст чата.')
    print('2. Отправить сообщение')
    print('0. Завершить')

    action = int(input('Введите 1, 2 или 0: '))

    if action == 0:
        break

    elif action == 1:
        read_file(current_directory)

    elif action == 2:
        write_file(current_directory)
