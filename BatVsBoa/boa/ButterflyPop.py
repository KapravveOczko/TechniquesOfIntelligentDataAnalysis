import random


class ButterflyPop:

    def __init__(self, function):
        self.function = function
        self.butterfly_pop = []
        # a
        self.force = 0
        # l
        # self.stimulus = stimulus

    def append_butterfly(self, butterfly):
        self.butterfly_pop.append(butterfly)

    def set_force(self, i, iters):
        self.force = 0.1 + 0.2 * i / iters

    def random_insects(self):
        return random.sample(self.butterfly_pop, 2)

    def get_stimulus(self, i, boa_best_coordinates):
        return self.butterfly_pop[i]/(boa_best_coordinates + 2.2204e-16)
