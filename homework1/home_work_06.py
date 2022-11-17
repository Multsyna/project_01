# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

from cmath import exp


salary = float(input('зарплата сотрудника: '))
expenses = float(input('расходы в месяц: '))

month = [1,2,3,4,5,6,7,8,9,10,11,12]
exp = 0


if salary >= expenses:
    print('условия не соотв')
else:
    for i in month:
        if i != 1:
            exp_total = expenses * i
            expenses = expenses * 1.03
            all_salary = salary * i
            inp = abs(all_salary - exp_total)

    print('Необходимо занять денег на год: ', round(inp,2))

# Вот решение чуть покороче
# Решение 2
salary, expenses = 10000, 12000

i = expenses - salary
m = 0
debt = 0
while m < 12:
    mx = i * (1.03 ** m)
    debt += mx
    m += 1
print(f'Необходимо взять в долг {round(debt, 2)} рублей')


