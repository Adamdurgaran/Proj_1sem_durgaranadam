#Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
#Использовать локальные переменные.

def function_sum(a, b):
    sum = 0
    while a <= b:
        sum = sum + a
        a = a + 1
    return sum
a = float(input('Введите первое число: '))
b = float(input('Введите последнее число: '))
s = function_sum(a, b)
print('Сумма ряда чисел: ', s)