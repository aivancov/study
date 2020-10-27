class Rating:
    def __init__(self, array):
        self.array = array
        self.array.sort(reverse=True)

    def __str__(self):
        return f'Current rating list: {self.array}'

    def insert(self, number):
        self.array.append(number)
        self.array.sort(reverse=True)

rating = Rating(
    [7, 1, 4, 3]
)
print(rating)


while True:
    number = input('Please enter new rating. Press "q" to exit. ')
    if number == 'q':
        break
    try:
        number = int(number)
    except ValueError:
        print('Rating must be integer.')
        continue
    rating.insert(number)
    print(rating)
