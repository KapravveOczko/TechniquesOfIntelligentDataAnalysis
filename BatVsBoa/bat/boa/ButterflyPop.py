class ButterflyPop:

    def __init__(self, function):
        self.function = function
        self.butterfly_pop = []
        self.best_butterfly_value = None
        self.best_butterfly = None
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
