# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

import numpy as np

row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))

matrix = np.random.randint(-3, 3, (row, col))

print('Исходная матрица:')
print(matrix)
print('Среднее арифметическое для каждой строки с нечетным номером:')
print(*('{} = {}'.format(i, sum(i)/len(i)) for i in matrix[::2]), sep='\n')

