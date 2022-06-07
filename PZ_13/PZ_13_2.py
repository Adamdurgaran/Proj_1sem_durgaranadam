towns = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
not_this = ['а', 'е', 'о', 'у', 'э', 'я', 'ю', 'ё', 'и']
output = []
for i in towns:
    i = i.lower()
    for j in i:
        if not j in not_this:
            output.append(j.upper())
print(' '.join(output))