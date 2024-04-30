import random
import numpy as np


class Bat:

    def __init__(self, x, frequency_min, frequency_max, alpha, epsilon):
        self.x = x
        self.velocity = 0

        self.score = 0

        self.frequency_min = frequency_min
        self.frequency_max = frequency_max
        self.frequency = 0
        self.set_frequency()

        self.volume = random.uniform(1, 2)
        # emision = r
        self.emission = random.random()

        self.alpha = alpha
        self.epsilon = epsilon

    def set_frequency(self):
        self.frequency = self.frequency_min + (self.frequency_max - self.frequency_min) * random.random()

    def set_score(self, function):
        self.score = function(self.x)

    def set_velocity(self, best_bat_x):
        self.velocity = self.velocity + (best_bat_x - self.x) * self.frequency

    def set_position(self):
        self.x = self.x + self.velocity

    def set_position_after_setting_position(self, average_volume):
        if random.random() < self.emission:
            self.x = self.x + random.random() * average_volume

    def set_volume(self):
        self.volume = self.alpha * self.volume

    def set_emission(self):
        self.emission = self.emission * (1 - np.exp(-self.epsilon))
