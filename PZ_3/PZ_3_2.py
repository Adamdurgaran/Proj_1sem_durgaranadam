#Дан номер года (положительное целое число).
#Определить количество дней в этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366 дней.
#Високосным считается год, делящийся на 4,
#за исключением тех годов, которые делятся на 100 и не делятся на 400
#(например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 — являются).

year = input('Введите номер года: ')
while type(year) != int:
    try:
        year = int(year)
        if year < 0:
            print('Вы ввели отрицательное число!')
            year = input('Введите положительное число: ')
    except ValueError:
        print('Введено не номер года!')
        year = input('Введите номер года: ')

if year % 4 != 0:
    print('В этом году 365 дней')
elif year % 100 != 0:
    print('В этом году 366 дней')
elif year % 400 != 0:
    print('В этом году 365 дней')
else:
    print('В этом году 366 дней')