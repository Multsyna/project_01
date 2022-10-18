# Задача 3
# Есть словарь списков количества товаров на складе.
# Рассчитать на какую сумму лежит каждого товара на складе
# Вывести стоимость каждого товара на складе: один раз распечатать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}




# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


search_result = goods[input('введите товар:  ')]

quantiti = store[search_result][0]['quantiti']
print(quantiti)




while True:
    user_input = input(f'Введите искомый товар из списка\n{list(goods)}: ')
    try:
        search_result = goods[user_input]
        break
    except KeyError: 
        print(f'Такого товара нет!', end='. ')

quantity = 0
for dict in store[search_result]:
    quantity += dict['quantity']

price = 0
for dict in store[search_result]:
    price += dict['price']

print(f'{user_input} - {quantity} шт, стоимость {price} руб')
