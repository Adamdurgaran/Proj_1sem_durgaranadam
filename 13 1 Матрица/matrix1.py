from random import randint

numbers = []
k = randint(1, 5)
for i in range(k):
    numbers.append([])
for i in range(k):
    for j in range(k):
        numbers[i].append(randint(-100, 100))
for i in range(0, k, 2):
    average = int(sum(numbers[i]) / len(numbers[i]))
    print(average)

