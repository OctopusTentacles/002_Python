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
        print('\n', read_chat.read())


def write_file(cur_dir, name):
        with open(os.path.join(cur_dir, 'chat.txt'), 
              'a', encoding='utf8') as text_chat:
            text_chat.write('{:<10}'.format(name + ':') + input('') + '\n')


# MAIN_CODE====================================================================

current_directory = os.path.dirname(__file__)

while True:

    user_name = input('\nВведите имя пользователя: ')
    if not user_name:
        break
    print('1. Посмотреть текущий текст чата.')
    print('2. Отправить сообщение')

    action = int(input('Введите 1 или 2: '))

    if action == 1:
        read_file(current_directory)

    elif action == 2:
        write_file(current_directory, user_name)

    else:
        break
