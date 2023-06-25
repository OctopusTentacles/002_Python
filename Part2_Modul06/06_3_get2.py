# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, 
# в которой он играет, а также его текущий статус, в котором указано, 
# отдыхает он, тренируется или путешествует:

# Напишите программу, которая выводит на экран следующие данные в разных строках:

# Все члены команды А, которые отдыхают.
# Все члены команды B, которые тренируются.
# Все члены команды C, которые путешествуют.

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
} 


a_rest = [player['name'] for player in players_dict.values() 
          if player['team'] == 'A' and player['status'] == 'Rest']
        
b_training = [player['name'] for player in players_dict.values()     
              if player['team'] == 'B' and player['status'] == 'Training']

c_travel = [player['name'] for player in players_dict.values() 
            if player['team'] == 'C' and player['status'] == 'Travel']

print('Все члены команды А, которые отдыхают', a_rest)
print('Все члены команды B, которые тренируются', b_training)
print('Все члены команды C, которые путешествуют', c_travel)
