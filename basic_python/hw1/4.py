def find_biggest_digit(number):
    '''Function to find the biggest digit of a number'''

    try:
        number = str( abs( int(number) ) )
    except ValueError:
        print(f'Invalid input. Integer expected but got {type(number)}: {number}')
        return

    max_digit = '0'
    i = len(number)-1
    while i >= 0:
        if number[i] > max_digit:
            max_digit = number[i]
        i -= 1

    return max_digit


number = input('Enter positive integer: ')
result = find_biggest_digit(number)
print(f'The biggest digit was: {result}')
