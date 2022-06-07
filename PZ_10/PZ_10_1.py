from random import randint

file = open('file1.txt', 'w+')
numbers = []
for i in range(randint(1, 20)):
    numbers.append(randint(-100, 100))
numbers = ' '.join(map(str, numbers))
file.write(numbers)
file.close()
file = open('file1.txt').read()
output = open('file2.txt', 'w+', encoding = 'utf-8')
output.write('Исходные данные: ' + file + '\n')
numbers = list(map(int, file.split(' ')))
output.write('Количество элементов: ' + str(len(numbers)) + '\n')
k = 0
for i in range(len(numbers)):
    if numbers[k] < numbers[i]:
        k = i
output.write('Индекс первого максимального элемента: ' + str(k + 1) + '\n')
start = int(len(numbers) / 3)
end = int(len(numbers) - len(numbers) / 3) - int(len(numbers) % 3 == 0)
mult = 1
for i in range(start, end + 1):
    mult *= i
output.write('Произведение элементов средней трети: ' + str(mult))
output.close()