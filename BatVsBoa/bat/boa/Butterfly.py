import random
import numpy as np


class Butterfly:

    def __init__(self):
        self.x = 0

        # c
        self.sensory = random.random()
        # f
        self.smell = 0

    def snif(self, stimulus, force):
        self.smell = self.sensory * np.power(stimulus, force)

    def move_to_the_best(self, best_value):
        self.x = self.x + (np.power(random.random(), 2) * best_value - self.x) * self.smell

    # random_insect_position1 != random_insect_position2 != this butterfly
    def move(self, random_insect_position1, random_insect_position2):
        self.x = self.x + (np.power(random.random(), 2) * random_insect_position1 - random_insect_position2) * self.smell
