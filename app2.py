import random

my_kub = [1, 2, 3, 4, 5, 6]

x = random.sample(my_kub,4)
print(x)
print(sum(x))
#####################################

import random
arr = int(input('ВВедите длину парля: '))

x = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
password = random.sample(x,arr)
print(f'ваш пароль : {password}')

if arr != int(arr):
    print('error')












