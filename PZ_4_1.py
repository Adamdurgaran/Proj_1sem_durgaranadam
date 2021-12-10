#Найти A в степени N
A = input('Введите вещественное число: ')
while type(A) != float:
    try:
        A = float(A)
    except ValueError:
        print('Введено не вещественное число!')
        A = input('Введите вещественное число: ')

N = input('Введите целую положительную степень: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введена не целая положительная степень!')
        N = input('Введите целую положительную степень: ')

if N > 0:
    i = 0
    while i < N:
        i += 1
        A = A ** N
        print(A)
else:
    print('Число N < 0!')


