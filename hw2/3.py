seasons = {
    0: 'Winter',
    1: 'Spring',
    2: 'Summer',
    3: 'Autumn'
}

months = [
    [1, 2, 12],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]


def which_season(number, months, seasons):
    for i in range(len(months)):
        if number in months[i]:
            return seasons[i]
    return

try:
    number = int(input('Please enter month number: '))
except ValueError:
    print('Wrong input. Integer expected')


season = which_season(number, months, seasons)
print(f'This is {season} month.' if season else 'Expected integer in range 1 - 12')
