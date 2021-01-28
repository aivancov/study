class Matrix:
    def __init__(self, *args):
        self.matrix = [array for array in args]
        self.size = len(args), len(args[0])

    def __str__(self):
        return '\n'.join([
            ' '.join([str(el) for el in array]) for array in self.matrix
        ])

    def __add__(self, other):
        added = [[i + j for i, j in zip(arr1, arr2)] for arr1, arr2 in zip(self.matrix, other.matrix)]
        return Matrix(*[array for array in added])


matrix1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9])
matrix2 = Matrix([1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1])
print(matrix1)
print()
print(matrix1.size)
print()

print(matrix1 + matrix2)