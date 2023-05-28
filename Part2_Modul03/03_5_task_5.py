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
    for index in range(len(violator_songs)):
        for song in range(1, songs + 1):
            print(f'Название {song}-й песни: ', end='')
            chosen_song = input()
            if chosen_song in violator_songs:
                minutes += violator_songs[chosen_song][1]
            else:
                print('Такой песни нет в этом альбоме!')
    return minutes


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

print(f'Общее время звучания песен: {playlist(num_songs)}')