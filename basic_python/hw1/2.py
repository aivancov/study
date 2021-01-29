def time_converter(time):
    '''Function to convert seconds into human-readable format'''

    try:
        time = int(time)
    except ValueError:
        print(f'Invalid input. Integer expected but got {type(time)}: {time}')
        return

    if time < 0:
        print(f'Invalid input. Positive integer expected but got negative: {time}')
        return

    hours = int(time)//3600
    minutes = (int(time) % 3600) // 60
    seconds = int(time) % 60

    time_array = [hours, minutes, seconds]

    for i in range(len(time_array)):
        item = str(time_array[i])
        if len(item) == 1:
            item = '0' + item
        elif len(item) > 2:
            print('Too big value to display. Only remainder accepted.')
            item = item[-2:]
        time_array[i] = item

    return ':'.join(time_array)


time = input('Enter number of seconds: ')
str_time = time_converter(time)
print(f'{str_time}')