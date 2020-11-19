class Cell:
    def __init__(self, compartments):
        self.compartments = compartments

    def __str__(self):
        return f'This cell contains {self.compartments} compartments'

    def __add__(self, other):
        return Cell(self.compartments+other.compartments)

    def __sub__(self, other):
        if self.compartments > other.compartments:
            return Cell(self.compartments-other.compartments)
        print('Cannot subtract greater cell from the less one')
        return Cell(0)

    def __mul__(self, other):
        return Cell(self.compartments*other.compartments)

    def __truediv__(self, other):
        return Cell(int(self.compartments/other.compartments))

    def make_order(self, num):
        result = ''
        for i in range(self.compartments // num):
            result += '*'*num + '\n'
        result += '*'*(self.compartments % num)
        return result


cell1 = Cell(5)
cell2 = Cell(7)

print('Cell 1: ', cell1)
print(cell1.make_order(4))
print()
print('Cell 2: ', cell2)
print(cell2.make_order(4))
print()
print('Addition: ', (cell1 + cell2))
print((cell1 + cell2).make_order(5))
print()
print('Subtraction: ', (cell2 - cell1))
print((cell2 - cell1).make_order(3))
print()
print('Forbidden subtraction: ', (cell1 - cell2))
print((cell1 - cell2).make_order(5))
print()
print('Multiplication: ', (cell1 * cell2))
print((cell1 * cell2).make_order(8))
print()
print('Division: ', (Cell(100) / cell2))
print((Cell(100) / cell2).make_order(5))
print()
