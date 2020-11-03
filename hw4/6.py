from itertools import cycle, count

def list_of_integers(outset, limit):
    res = []
    for i in count(outset):
        if len(res) >= limit:
            return res
        res.append(i)


def repeat_list(array, limit):
    res = []
    for i in cycle(array):
        if len(res) >= limit:
            return res
        res.append(i)

array = [1, 2, 3, 4]
limit = 20

print(list_of_integers(5, limit))
print(repeat_list(array, limit))