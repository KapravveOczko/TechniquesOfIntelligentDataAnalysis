import random
import numpy as np
from math import inf

class Bat:

    def __init__(self, function_bounds, frequency_min, frequency_max, alpha, epsilon, dimensions):
        self.coordinates = [np.random.uniform(function_bounds['min'], function_bounds['max']) for i in range(dimensions)]
        self.velocity = np.zeros(dimensions)

        self.score = inf

        self.frequency_min = frequency_min
        self.frequency_max = frequency_max
        self.frequency = np.zeros(dimensions)
        self.set_frequency()

        self.volume = random.uniform(1, 2)
        # emission = r
        self.emission = random.random()

        self.alpha = alpha
        self.epsilon = epsilon

    def set_frequency(self):
        self.frequency = self.frequency_min + (self.frequency_max - self.frequency_min) * random.random()

    def set_score(self, function):
        self.score = function(self.coordinates)

    def set_velocity(self, best_bat_coordinates):
        self.velocity = self.velocity + (best_bat_coordinates - self.coordinates) * self.frequency

    def set_position(self):
        self.coordinates = self.coordinates + self.velocity

    def set_position_after_setting_position(self, average_volume):
        if random.random() < self.emission:
            self.coordinates = self.coordinates + random.uniform(-1, 1) * average_volume

    def set_volume(self):
        self.volume = self.alpha * self.volume

    def set_emission(self):
        self.emission = self.emission * (1 - np.exp(-self.epsilon))
