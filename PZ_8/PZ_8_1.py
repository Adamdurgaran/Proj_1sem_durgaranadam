# Организовать словарь 10 русско- английских слов, обеспечивающий
# "перевод" русского слова на английского.

dictionary = {'стул': 'chair', 'стена': 'wall', 'яблоко': 'apple', 'ручка': 'pen', 'дерево': 'tree', 'игра': 'game',
              'мяч': 'ball', 'страна': 'country', 'навык': 'skill', 'огонь': 'fire'}

word = input('Введите слово на русском: ')
print('Данное слово на английском:', dictionary[word])
