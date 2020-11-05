en_rus = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('f4_1.txt') as fin:
    with open('f4_2.txt', 'w') as fout:
        for line in fin.readlines():
            en, num = line.split(' — ')
            fout.write(' — '.join([en_rus[en], num]))
