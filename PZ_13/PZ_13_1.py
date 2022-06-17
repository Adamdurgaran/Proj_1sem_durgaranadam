# Проверить есть ли в последовательности целых N чисел число K

import random

N = []
k = 5

print('Данное число:', k)

for i in range(5):
    N.append(random.randint(1, 10))

print('Начальный список:', N)

if list(filter(lambda k: k == 5, N)):
    print('В списке есть данное число')
else:
    print('В списке нет данного числа')
