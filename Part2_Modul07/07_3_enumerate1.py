# Задача 1. Саботаж!
# Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам 
# и добавил в код сайта символ ~ (тильда). 
# Но программисты быстро решили эту проблему, пройдясь по всему коду 
# маленькой программой.

# Пользователь вводит строку. Напишите программу, 
# которая проходит по строке и выводит в консоль индексы символа ~. 
# Для решения этой задачи (и остальных тоже) используйте функцию enumerate.

# Пример:
# Строка: so~mec~od~e
# Ответ: 2 6 9 

word = input('Строка: ')

i_index = [index for index, i_value in enumerate(word) if i_value == '~']

print('Ответ:', *i_index)

# ___________________________________________________________________________

def get_indexes(where_to_search, what_to_search):
    return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]


text = input("Введите текст: ")
print("Ответ:", " ".join(get_indexes(text, "~")))
