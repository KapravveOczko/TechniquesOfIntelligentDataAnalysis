class Entity:

    def __init__(self, coordinates, func):
        self.coordinates = coordinates
        self.value = func(coordinates)

    def calculate_best_value(self):
        self.value = self.func(self.coordinates)