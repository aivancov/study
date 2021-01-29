from pprint import pprint
import json

def format_value(str_value):
    return int(''.join([i for i in str_value if i.isdigit()]))


with open('f7_1.txt') as fin:
    total_profit = 0
    stats = {}
    for i, line in enumerate(fin.readlines()):
        name, _, income, costs = line.split()
        income, costs = map(format_value, [income, costs])
        profit = income - costs
        stats[name] = profit
        if income - costs > 0:
            total_profit += profit
    result = [stats, {'average_profit': round(total_profit/i)}]
    pprint(result)

with open('f7_2.txt', 'w') as fout:
    fout.write(json.dumps(result, indent=4))
