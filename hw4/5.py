from functools import reduce


def multiply(a, b):
    return a * b

print(
    reduce(multiply, [i for i in range(100, 1002, 2)])
)