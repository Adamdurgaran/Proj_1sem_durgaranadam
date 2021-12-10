# Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
# значение A переходит в B, значение B — в C, значение C — в A (A, B, C — вещественные
# параметры, являющиеся одновременно входными и выходными). С помощью этой функции
# выполнить правый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1)
# и (A2, B2, C2).

def ShiftRight3(A, B, C):
    num = C
    C = B
    B = A
    A = num
    return A, B, C

print('Введите первый набор чисел: ')
A1 = float(input(''))
B1 = float(input(''))
C1 = float(input(''))
print('Введите второй набор чисел: ')
A2 = float(input(''))
B2 = float(input(''))
C2 = float(input(''))

k = ShiftRight3(A1, B1, C1)
print(k)
k = ShiftRight3(A2, B2, C2)
print(k)



