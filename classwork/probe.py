# файл для тестов
from pprint import pprint 

capitals = {} 

capitals['Россия']= 'Москва'
capitals['Франция']= 'Париж'
capitals['Италия']= 'Рим'

print(capitals)

cities =capitals 
cities['бразилия']='Бразилиа'

print(cities)
# кортеж неизменяемый объект

my_tuple = (20, 30, 40)
new_tuple = my_tuple
new_tuple += (50,60)

print(my_tuple,'\n', new_tuple )


print(cities,'\n',capitals)














