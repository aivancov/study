def int_func(word):
    return word.title()

def format_line(line):
    return ' '.join([int_func(word) for word in line.split()])


if __name__ == "__main__":
    print(int_func('Text'))
    print(format_line('nothing else matters.'))