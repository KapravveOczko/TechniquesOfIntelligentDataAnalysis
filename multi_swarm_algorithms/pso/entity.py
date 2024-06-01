import numpy as np
import random

class Entity:
    def __init__(self, dimensions, func, bounds):
        self.position = np.array([random.uniform(bounds['min'], bounds['max']) for _ in range(dimensions)])
        self.velocity = np.array([random.uniform(-1, 1) for _ in range(dimensions)])
        self.value = func(self.position)
        self.func = func
        self.best_value = self.value
        self.best_position = self.position

    def calculate_new_position(self):
        self.value = self.func(self.position)
        if self.value < self.best_value:
            self.best_value = self.value
            self.best_position = self.position

    def update_velocity(self, global_best_position, c1, c2, w):
        r1 = np.random.rand(self.position.size)
        r2 = np.random.rand(self.position.size)
        cognitive_velocity = c1 * r1 * (self.best_position - self.position)
        social_velocity = c2 * r2 * (global_best_position - self.position)
        self.velocity = w * self.velocity + cognitive_velocity + social_velocity

    def update_position(self):
        self.position += self.velocity
        self.calculate_new_position()