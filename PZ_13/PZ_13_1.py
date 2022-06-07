from random import randint

numbers = []
for i in range(randint(1, 20)):
    numbers.append(randint(-100, 100))
k = int(input())
is_here = False
for i in numbers:
    if i == k:
        is_here = True
if is_here:
    print('K есть в последовательности.')
else:
    print('K нет в последовательности.')