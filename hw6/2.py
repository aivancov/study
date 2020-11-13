class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, density, thickness):
        return self._length * self._width * density * thickness

road = Road(1000, 9)
print(road.calculate_mass(80, 10))
