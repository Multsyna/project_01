#домашние задания
# Задача 2 ГОТОВА
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек


from numpy import gradient


cities =[['Москва', 11.92], ['Питер', 4.99], ['Рязань', 0.53], ['Самара', 1.17], ['Волгоград', 1.01]]



print(f'Население {cities[1][0]} - {cities[1][1]} человек')

totalCount = 0


for city in cities: 
   totalCount += city[1] 
   

print(f'Итого размер населения - {totalCount} человек')


# Задача 3
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]







# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

for









