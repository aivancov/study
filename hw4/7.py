def fact(n):
    i = 1
    for num in range(1, n+1):
        i *= num
        yield i


for el in fact(6):
    print(el)
