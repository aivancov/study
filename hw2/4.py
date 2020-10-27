line = input('Введите слова, разделенные пробелами: ')

for i, word in enumerate(line.split()):
    print(f'{i}. {word[:10]}')
