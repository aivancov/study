def calculate_dummy_number(number):
    '''Function to construct number like nnn from number n'''

    try:
        number = int(number)
    except ValueError:
        print(f'Invalid input. Integer expected but got {type(number)}: {number}')
        return

    assert 0 < number < 10, f'Invalid input. One digit expected, but got {number}'
    return 111 * number


number = input('Enter one digit: ')
print(calculate_dummy_number(number))
