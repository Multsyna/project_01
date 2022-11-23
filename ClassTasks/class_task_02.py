# Задача 2
# Есть словарь координат городов sites, 
# Составьте словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

from pprint import pprint
from turtle import distance



sites = {
    'Москва': (550, 370),
    'Лондон': (510, 510),
    'Париж': (480, 480),
}

distances = {}
moscow_to_paris = (sites['Москва'][0] - sites['Лондон'][0])** 2 + (sites['Москва'][1] - sites['Лондон'][1])** 2
moscow_to_london = (sites['Москва'][0] - sites['Париж'][0])** 2 + (sites['Москва'][1] - sites['Париж'][1])** 2
london_to_paris = (sites['Москва'][0] - sites['Лондон'][0])** 2 + (sites['Москва'][1] - sites['Лондон'][1])** 2

distances['Москва'] = {
    'Лондон': moscow_to_london,
    'Париж': moscow_to_paris,
    }
distances['и тд.'] = {}

# здесь заполнение словаря

pprint(distances)