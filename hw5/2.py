with open('f2.txt') as fin:
    print(f'Количество строк в файле: {len(fin.readlines())}')
    fin.seek(0)
    for i, line in enumerate(fin.readlines(), 1):
        print(f'Количество слов в {i} строке: {len(line.split())}')
