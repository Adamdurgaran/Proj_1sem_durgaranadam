# Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 2
# + . . . + K будет больше или равна N, и саму эту сумму.
N = input("Введите целое положительное число: ")
while type(N) != int:
    try:
        N = int(N)
        if N < 1:
            print("Введите положительное число")
        else:
            break
    except ValueError:
        print("Введите число!")
        N = input("Введите число: ")
K = 0
S = 0
while S < N:
    S += K
    if S < N:
        K += 1
    if S >= N:
        print("Наименьшее число: {}".format(K))
        print("Сумма равна: {}".format(S))




