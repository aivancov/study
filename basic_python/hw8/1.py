import random
# random.seed(23)


class Generator:
    def __init__(self):
        self.barrels = list(range(1, 91))
        # print(self.barrels)

    def generate_barrel(self):
        return self.barrels.pop(random.randint(0, len(self.barrels)-1))

    def generate_indexes(self, num):
        all_indexes = list(range(num))
        chosen_indexes = []
        for i in range(5):
            chosen_indexes.append(all_indexes.pop(random.randint(0, len(all_indexes)-1)))
        return chosen_indexes


class Card:

    def __init__(self, name):
        self.name = name
        self.matrix = []
        self.generator = Generator()
        self.total_digits = 15

    def generate(self):
        for i in range(3):
            line = ['_' for _ in range(9)]
            numbers = sorted([self.generator.generate_barrel() for _ in range(5)])
            indexes = sorted(self.generator.generate_indexes(len(line)))
            for key, value in zip(indexes, numbers):
                line[key] = value

            self.matrix.append(line)

    def __str__(self):
        return f'{self.name:-^30}' + '\n' + '\n'.join([
            '  '.join([str(el) for el in array]) for array in self.matrix
        ]) + '\n' + '-' * 30

    def find_number(self, number):
        for i, line in enumerate(self.matrix):
            for j, el in enumerate(line):
                if el == number:
                    return (i, j)
        return

    def delete_value(self, y, x):
        self.matrix[y][x] = 'x'
        self.total_digits -= 1


def game():
    user_card = Card('User card')
    comp_card = Card('Computer card')
    user_card.generate()
    comp_card.generate()
    generator = Generator()
    winner = ''
    in_game = True

    while in_game:
        barrel = generator.generate_barrel()
        print(f'\nНовый бочонок: {barrel} (осталось {len(generator.barrels)})')
        print(user_card)
        print(comp_card)
        resp = input('Зачеркнуть цифру? y/n ')
        barrel_user_index = user_card.find_number(barrel)
        barrel_comp_index = comp_card.find_number(barrel)
        if (resp == 'y' and not barrel_user_index) or (resp == 'n' and barrel_user_index):
            winner = 'Computer'
            in_game = False
        elif resp == 'y':
            user_card.delete_value(barrel_user_index[0], barrel_user_index[1])

        if barrel_comp_index:
            comp_card.delete_value(barrel_comp_index[0], barrel_comp_index[1])

        for player in [user_card, comp_card]:
            if player.total_digits == 0:
                winner = player.name
                in_game = False

    print(f'{winner} wins!')
    return


if __name__ == "__main__":
    game()
