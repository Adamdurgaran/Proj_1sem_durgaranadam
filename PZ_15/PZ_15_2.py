# В матрице найти максимальный положительный элемент, кратный 4.

from random import randint

row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))

matrix = [[randint(-100, 100) for j in range(col)] for i in range(row)]

print('Исходная матрица:', matrix)

r = lambda value: value > 0 and value % 4 == 0

max_value = 0
for n, m in enumerate(matrix):
    for n1, m1 in enumerate(m):
        if r(m1):
            if m1 > max_value:
                max_value = m1

print('Максимальный положительный элемент, кратный 4:', max_value)
