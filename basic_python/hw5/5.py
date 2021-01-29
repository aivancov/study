import random

COUNT = 10
with open('f5.txt', 'w') as fout:
    nums = [str(random.randint(1, 100)) for i in range(COUNT)]
    fout.write(' '.join(nums))

with open('f5.txt') as fin:
    total = sum([int(num) for num in fin.read().strip().split()])
    print(f'Сумма чисел: {total}')
