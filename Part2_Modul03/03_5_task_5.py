# Задача 5. Песни

# Мы пишем приложение для удобного прослушивания музыки. 
# У Вани есть список из девяти песен группы Depeche Mode. 
# Каждая песня состоит из названия и продолжительности с точностью до долей минут:

# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый 
# плейлист с другими треками. И при этом ему важно, 
# сколько времени в сумме эти N песен будут звучать.

# Напишите программу, которая запрашивает у пользователя 
# количество песен из списка и затем названия этих песен, 
# а на экран выводит общее время их звучания.

# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean

# Общее время звучания песен: 14.93 минуты


def playlist(songs):
    minutes = 0
  
    for song in range(1, songs + 1):
        
        while True:
            print(f'Название {song}-й песни: ', end='')
            chosen_song = input()
            if input_check(chosen_song):
                break
            else:
                print('Такой песни нет в этом альбоме! Повторите ввод!')  
        
        for index in range(len(violator_songs)):
            if violator_songs[index][0] == chosen_song:
                 minutes += violator_songs[index][1]
                 break
    return minutes


def input_check(chosen_song):
    for index in range(len(violator_songs)):
        if chosen_song in violator_songs[index][0]:
            return True


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs = int(input('Сколько песен выбрать? '))

print(f'\nОбщее время звучания песен: {round(playlist(num_songs), 2)} минуты.')