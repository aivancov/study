def filter_non_digit(line):
    return any([i.isdigit() for i in line])

hours = {}

with open('f6.txt') as fin:
    for line in fin.readlines():
        subj, *hrs_str = line.split()
        total = sum([int(''.join([l for l in num if l.isdigit()])) for num in filter(filter_non_digit, hrs_str)])
        hours[subj] =  total

print(hours)
