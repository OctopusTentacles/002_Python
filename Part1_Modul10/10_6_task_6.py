print('Задача 6. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#".
# Пусть высота пирамиды вводится пользователем.

# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

#
###
#####
#######

h = int(input('Высота пирамиды будет: '))

for row in range(h):
    for col in range(7):
        if col == 4:
            print('*', end='')
        print(' ', end='')
    print()
