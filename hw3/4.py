def my_func1(x, y):
    return x**y

def my_func2(x, y):
    result = 1
    for i in range(-y):
        result *= x
    return 1/result


if __name__ == "__main__":
    x, y = 2.7, -7
    print(my_func1(x, y))
    print(my_func2(x, y))
