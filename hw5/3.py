with open('f3.txt') as fin:
    total = 0
    for i, line in enumerate(fin.readlines(), 1):
        surname, income = line.split()
        income = int(income)
        if income < 20000:
            print(surname)
        total += income
    print(f'Средний доход: {total/i}')
