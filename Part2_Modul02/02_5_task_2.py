# Задача 2. Турнир

# Что нужно сделать
# Для соревнований по волейболу необходимо сформировать турнирнирную 
# сетку из восьми человек на два дня. На первый день из списка 
# участников решили выбрать каждого второго.

# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, 
# Евгений, Женя, Захар. Напишите программу, которая выводит 
# элементы списка только с чётными индексами.

# Пример:

# Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']

team_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_team = []

for index in range(len(team_list)):
    if index % 2 == 0:
        first_team.append(team_list[index])

print('Первый день:', first_team)