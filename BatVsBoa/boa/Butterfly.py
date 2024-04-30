import random
import numpy as np


class Butterfly:

    def __init__(self):
        self.x = 0

        # c
        self.sensory = 0.01
        # f
        self.smell = 0

    def snif(self, stimulus, force):
        self.smell = self.sensory * np.power(stimulus, force)

    def move_to_the_best(self, r, best_value):
        self.x = self.x + (np.power(r, 2) * best_value - self.x) * self.smell

    # random_insect_position1 != random_insect_position2 != this butterfly
    def move(self, r, random_insect_position1, random_insect_position2):
        self.x = (self.x + (np.power(r, 2) * random_insect_position1 - random_insect_position2)
                  * self.smell)

    def move_to_the_best_levy_style(self, levy, best_value):
        self.x = self.x + levy * (best_value - self.x) * self.smell

    # random_insect_position1 != random_insect_position2 != this butterfly
    def move_levy_style(self, levy, random_insect_position1, random_insect_position2):
        self.x = self.x + levy * (random_insect_position1 - random_insect_position2) * self.smell
