array = input('Введите элементы через пробел: ').split()

print(f'Initial array: {array}')
for i in range(1, len(array), 2):
    array[i], array[i-1] = array[i-1], array[i]

print(f'Mutated array: {array}')