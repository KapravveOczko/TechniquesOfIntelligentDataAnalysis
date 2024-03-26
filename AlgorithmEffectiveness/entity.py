class Entity:

    def __init__(self, coordinates, func):
        self.coordinates = coordinates
        self.value = func(coordinates)
        self.func = func
        self.best_value = self.value
        self.best_coordinates = self.coordinates

    def calculate_best_value(self):
        self.value = self.func(self.coordinates)
        if self.value < self.best_value:
            self.best_value = self.value
            self.best_coordinates = self.coordinates