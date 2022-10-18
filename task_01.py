#Задание Сделано
# Есть строка с перечислением песен    

from ast import arg


my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

first_song = my_favorite_songs[0:my_favorite_songs.find(',')]

print(len(my_favorite_songs))

print(first_song)


last_song = my_favorite_songs[my_favorite_songs.find('New'):77]
print(last_song)

second_song = my_favorite_songs[len(first_song) + 2:my_favorite_songs.find(', A')]
print(second_song)

last_song2 = my_favorite_songs[my_favorite_songs.find('Start'):77 - len(last_song)]

print(last_song2)



#argSong = my_favorite_songs.split(',')


#print(argSong[0])
#print(argSong[1])
#print(argSong[-1])
#print(argSong[-2])


