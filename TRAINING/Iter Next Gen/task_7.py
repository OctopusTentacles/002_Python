# Example for send

from random import choice

def song_generator(song_list):
    new_song = None

    while True:
        if new_song != True:
            if new_song not in song_list:
                song_list.append(new_song)



songs = ["Her Şeyi Yak - Sezen Aksu", 
         "Bluesette - Toots Thielemans",
         "Six Marimbas - Steve Reich",
         "Riverside - Agnes Obel",
         "Not for Radio - Nas",
         "What's going on - Taste",
         "On Stream - Nils Petter Molvær",
         "La' Inta Habibi - Fayrouz",
         "Ik Leef Niet Meer Voor Jou - Marco Borsato",
         "Δέκα λεπτά - Αθηνά Ανδρεάδη"]

radio_program = song_generator(songs)