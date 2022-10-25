# Задача 5
# Приведем плейлист песен в виде словаря
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import pprint
import random

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
mylist = random.sample(list(my_favorite_songs),3)
# print(mylist)
total_count = 0
for song in mylist:
    total_count += my_favorite_songs[mylist[1]]


print(f'три песни звучат- {total_count}')