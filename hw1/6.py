def find_first_good_day(dist, goal):
    '''Searching for the first day when the goal has been achieved'''

    day = 1
    while dist < goal:
        dist *= 1.1
        day += 1

    return day


distance = int(input('Введите результат первого забега: '))
goal = int(input('Введите желаемый результат: '))

days = find_first_good_day(distance, goal)
print(days)
