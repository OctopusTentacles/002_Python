# Задача 1. Задачи компаний

# Одна IT-компания решила расшириться и взяла под своё крыло ещё три таких же, 
# но поменьше. Конечно же, все выполненные и невыполненные задачи этих 
# компаний перетекли в основную компанию.

# Даны четыре списка компаний, в которых для каждой задачи написано, 
# выполнена (1) она или нет (0):

# Напишите программу, которая расширяет список main элементами 
# остальных списков, выведите итоговый список, 
# а также выведите количество невыполненных задач.

# Результат работы программы:
# Общий список задач: [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]
# Кол-во невыполненных задач: 10



main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

first_company = [0, 0, 0]

second_company = [1, 0, 0, 1, 1]

third_company = [1, 1, 1, 0, 1]
