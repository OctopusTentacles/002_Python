# Задача 1. Робот
# В одном отеле для эксперимента на вход хотят поставить робота,
# который будет спрашивать у прохожих, не желают ли они зайти.
# При ответе «Да» робот должен приветствовать человека и пустить в отель.
# Для робота написали вот такую программу с использованием функции:
# Def greeting()
#   print('Привет!')
# print('Добро пожаловать!')
# while True:
#   a = input('Зайдёте? Да/Нет: ')
#   if a = 'Да':
#       greeting
#   print('Следующий.\n')

# Однако программист очень торопился и допустил несколько ошибок.

# Скопируйте программу в реплит, найдите и исправьте ошибки.
# Убедитесь, что программа работает корректно.
# Пример результата:

# Зайдёте? Да/Нет: Да
# Привет!
# Добро пожаловать!
# Следующий.

# Зайдёте? Да/Нет: Да
# Привет!
# Добро пожаловать!
# Следующий.

# Зайдёте? Да/Нет: Нет
# Следующий.

# Зайдёте? Да/Нет: ...

Def greeting()
print('Привет!')

print('Добро пожаловать!')

while True:
    a = input('Зайдёте? Да/Нет: ')
    if a = 'Да':
    greeting
    print('Следующий.\n')
