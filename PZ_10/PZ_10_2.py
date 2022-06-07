import re

file = open('text18-13.txt', encoding = 'utf-8').read() + '\n'
file_new = open('file_new.txt', 'w+', encoding = 'utf-8')
n = int(input('После какой строки будет вставлена фраза? '))
phrase = input('Введите фразу: ')
lenght = len(file) - 7
print()
print(file)
if n == 0:
    file = phrase + '\n' + file[1::]
else:
    file = list(file)
    phrase = list(phrase)
    counter = 0
    for i in range(len(file)):
        if file[i] == '\n':
            counter += 1
        if counter == n:
            for j in range(len(phrase)):
                file.insert(i + j + 1, phrase[j])
            file.insert(i + j + 2, '\n')
            file = ''.join(file)
            break
file_new.write(file)
print(str(lenght) + ' симв.')