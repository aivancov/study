def evaluate_reliability(income, costs):
    '''Function to compare income and costs'''

    income = int(income)
    costs = int(costs)

    rent = None
    if income > costs:
        print('Фирма получает прибыль.')
        rent = income/costs
    elif income < costs:
        print('Фирма работает в убыток')
    else:
        print('Фирма выходит в ноль.')

    return rent


income = input('Введите доход фирмы: ')
costs = input('Введите издержки фирмы: ')

rent = evaluate_reliability(income, costs)

if rent:
    print(f'Рентабельность выручки: {rent}')
    staff = input('Введите количество сотрудников фирмы: ')
    profit = (int(income) - int(costs))/int(staff)
    print('Прибыль фирмы в расчете на одного сотрудника: {:.2f}'.format(profit))
