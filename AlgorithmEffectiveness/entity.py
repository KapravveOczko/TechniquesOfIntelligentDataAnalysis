import random


def initialize_vector(a, b, size):
    vector = []
    for i in range(size):
        vector.append(random.uniform(a, b))
    return vector


class Entity:

    def __init__(self, a, b, size):
        self.vector = initialize_vector(a, b, size)
        self.adaptation_score = 0
