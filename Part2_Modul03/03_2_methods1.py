# Задача 1. Зоопарк

# В маленьком зоопарке каждое животное сидит в отдельной клетке, 
# всего этих животных четверо: лев, кенгуру, слон и обезьяна. 
# В базе данных они хранятся в виде вот такого списка:

# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Сегодня в зоопарк завезли медведя (bear) и посадили его между 
# львом и кенгуру. В итоге животных стало пять. 
# А через неделю слона перевезли в другое место и в списке снова стало четверо животных.

# Реализуйте эти действия в коде программы и выведите в консоль итоговый 
# список животных, а также покажите, в какой клетке сидят лев и обезьяна. 
# Для этого используйте методы списков.

# Результат работы программы:
# Зоопарк: ['lion', 'bear', 'kangaroo', 'monkey']
# Лев сидит в клетке номер 1
# Обезьяна сидит в клетке номер 4

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(1, 'bear')
zoo.remove('elephant')

print('Зоопарк', zoo)