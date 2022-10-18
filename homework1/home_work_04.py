# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

from calendar import month

#Вариант 1

year = ['222', '31', '28', '31', '30', '30', '31', '30', '10', '23', '30', '31', '22']


user_input = input("Введите номер месяца: ")

if 12 >= int(user_input) > 0:
    print('Количество дней в этом месяце:', year[int(user_input) - 1])
else:
   print('номер месяца некорректен')

#Вариант 2

#month = int(user_input)

#if month == 1:
#    print('Количество дней: 31')
#elif month == 2:
#    print('Количество дней: 28')
#else:
#    print('номер месяца некорректен')