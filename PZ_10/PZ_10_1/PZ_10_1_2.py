from random import randint

file = open('file1.txt', 'w+')
numbers = []
for i in range(randint(1, 20)):
    numbers.append(randint(-100, 100))
numbers = ' '.join(map(str, numbers))
file.write(numbers)
file.close()