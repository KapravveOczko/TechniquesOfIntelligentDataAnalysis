import random


class ButterflyPop:

    def __init__(self, function):
        self.function = function
        self.butterfly_pop = []
        self.best_butterfly_value = 0
        self.best_butterfly = 0
        # a
        self.force = 0
        # l
        # self.stimulus = stimulus

    def get_best_butterfly(self):
        best = 0
        best_x = 0
        for insect in self.butterfly_pop:
            if best < self.function(insect.x):
                best = self.function(insect.x)
                best_x = insect.x

        self.best_butterfly, self.best_butterfly_value = best_x, best

    def append_butterfly(self, butterfly):
        self.butterfly_pop.append(butterfly)

    def set_force(self, i, iters):
        self.force = 0.1 + 0.2 * i / iters

    def random_insects(self):
        random_insect1, random_insect2 = 0, 0
        x = True

        while x:
            random_insect1 = self.butterfly_pop[random.randint(0, len(self.butterfly_pop)-1)]
            random_insect2 = self.butterfly_pop[random.randint(0, len(self.butterfly_pop)-1)]
            if random_insect1 != random_insect2:
                x = False

        return random_insect1, random_insect2

    def get_stimulus(self, i):
        return self.butterfly_pop[i]/(self.best_butterfly_value + 2.2204e-16)
