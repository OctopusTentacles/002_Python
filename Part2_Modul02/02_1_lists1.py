# Задача 1. Таблица степеней
# Аркадий как-то раз написал программу для вывода таблицы степеней для определённых чисел. 
# Недавно он узнал про такую штуку, как списки, и решил программу немного переписать, а заодно 
# усовершенствовать её. По его задумке, вначале есть всего три числа: 3, 7 и 5, а затем с 
# помощью бесконечного цикла программа запрашивает новое число, закидывает его в конец текущего 
# списка чисел и выводит вторую, третью и четвёртую степень каждого числа текущего списка. 
# Вот какая программа получилась у Аркадия:

# Однако, к сожалению, эта программа у него не заработала. 
# Помогите Аркадию исправить ошибки в коде. Убедитесь, что программа работает верно.

# Пример верного результата:
# Новое число: 1
# Текущий список чисел: [3, 7, 5, 1]
# 9 27 81
# 49 343 2401
# 25 125 625
# 1 1 1

# Новое число: 2
# Текущий список чисел: [3, 7, 5, 1, 2]
# 9 27 81
# 49 343 2401
# 25 125 625
# 1 1 1
# 4 8 16

numbers = [3,7,5]
while True:
    number = int(input('\nНовое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)
    for i in numbers:
        print(i ** 2, i ** 3, i ** 4, sep='\t')

