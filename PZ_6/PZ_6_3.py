# Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в
# A1, а исходное значение K первых элементов будет потеряно). Последние K элементов
# полученного списка положить равными 0.

from random import randint
N = int(input('Введите размер списка: '))
K = int(input('Введите K, с условием: 1 < K < N: '))
while (K < 1) or (K > N):
    print('K введено неверно!')
    K = int(input('Введите K: '))
a = []
i = 1
while N:
    a.append(randint(0, 100))
    N -= 1
    i += 1
print('Изначальный список: ', a)
shift = int(K)
a = a[shift:] + a[:shift]
for i in range(N-K, N):
    a[i] = 0
print('Со сдвигом влево на K позиций:', a)