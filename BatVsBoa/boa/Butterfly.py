import random
import numpy as np


class Butterfly:

    def __init__(self, function_bounds, dimensions):

        self.coordinates = np.random.uniform(function_bounds['min'], function_bounds['max'], dimensions)

        # c
        self.sensory = 0.01
        # f
        self.smell = 0

        self.score = np.inf

        self.sniff(random.random(), random.random())

    def calculate_score(self, function):
        self.score = function(self.coordinates)

    def sniff(self, stimulus, force):
        self.smell = self.sensory * np.power(stimulus, force)

    def move_to_the_best(self, r, best_value):
        self.coordinates = self.coordinates + (np.power(r, 2) * best_value - self.coordinates) * self.smell

    # random_insect_position1 != random_insect_position2 != this butterfly
    def move(self, r, random_insect):
        self.coordinates = (self.coordinates + (np.power(r, 2) * random_insect[0].coordinates - random_insect[1].coordinates) * self.smell)

    def move_to_the_best_levy_style(self, levy, best_value):
        self.coordinates = self.coordinates + levy * (best_value - self.coordinates) * self.smell

    # random_insect_position1 != random_insect_position2 != this butterfly
    def move_levy_style(self, levy, random_insect_position1, random_insect_position2):
        self.coordinates = self.coordinates + levy * (random_insect_position1 - random_insect_position2) * self.smell
