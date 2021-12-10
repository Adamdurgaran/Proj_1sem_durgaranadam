#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно из чисел A, B, C положительное».

a = input("Введите целое число A: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введено не целое число!')
        a = input('Введите целое число A: ')

b = input('Введите целое число B: ')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введено не целое число!')
        b = input('Введите целое число B: ')

c = input('Введите целое число C: ')
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Введено не целое число!')
        c = input('Введите целое число C: ')

if a >= 0 or b >= 0 or c >= 0:
    print('В ряде есть хотя бы одно положительнoе числo.')
else:
    print('В ряде нет положительных чисел')
