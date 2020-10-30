def sum_input():
    result = 0
    while True:

        line = input('Введите числа разделенный пробелом. Нажмите "q" для выхода: ')
        for item in line.split():
            if item == 'q':
                return result
            try:
                item = int(item)
                result += item
            except ValueError:
                pass
        print(f'Текущая сумма: {result}')
    return result


print(sum_input())
