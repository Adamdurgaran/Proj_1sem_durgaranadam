from random import randint

numbers = []
k = randint(1, 5)
for i in range(k):
    numbers.append([])
for i in range(k):
    for j in range(k):
        numbers[i].append(randint(-100, 100))
maximum = [0, 0]
for i in range(k):
    for j in range(len(numbers[i])):
        if numbers[i][j] % 4 == 0 and numbers[i][j] > 0:
            if numbers[maximum[0]][maximum[1]] < numbers[i][j]:
                maximum[0], maximum[1] = i, j
if maximum == [0, 0] and numbers[maximum[0]][maximum[1]] % 4 > 0:
    print('В матрице нет элементов, кратных 4.')
else:
    print(numbers)
    print('Элемент ' + str(maximum[0] + 1) + ' ряда ' + str(maximum[1] + 1) + ' столбца — ' + str(numbers[maximum[0]][maximum[1]]) + '.')