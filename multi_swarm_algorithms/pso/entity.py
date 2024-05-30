class Entity:
    def __init__(self, position, func):
        self.position = position
        self.value = func(position)
        self.func = func
        self.best_value = self.value
        self.best_position = self.position

    def calculate_new_position(self):
        self.value = self.func(self.position)
        if self.value < self.best_value:
            self.best_value = self.value
            self.best_position = self.position