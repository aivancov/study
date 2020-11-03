def divide(a, b):
    try:
        a, b = int(a), int(b)
    except ValueError:
        print('Invalid input')
        return
    try:
        return a/b
    except ZeroDivisionError:
        print('Non-zero denominator required')
        return


a = input('Please enter the numerator: ')
b = input('Please enter the denominator: ')

result = divide(a, b)
print(f'Result is: {result}'  if result else 'Invalid input')
