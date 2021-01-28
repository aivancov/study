with open('f1.txt', 'a') as fout:
    while True:
        text = input('Введите текст: ')
        if not text:
            break
        fout.write(text + '\n')
