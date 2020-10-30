def my_func(*args):
    return sum(sorted(list(args), reverse=True)[:2])


if __name__ == "__main__":
    print(my_func(2, 6, 4))
