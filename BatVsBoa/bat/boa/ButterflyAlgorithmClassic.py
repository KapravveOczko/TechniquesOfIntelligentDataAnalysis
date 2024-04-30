import random
from ButterflyPop import ButterflyPop
from Butterfly import Butterfly


def butterfly_algorithm_classic(iters, pop, function, stimulus, p=0.8):
    butterfly_pop = ButterflyPop(function)

    for i in range(pop):
        butterfly_pop.append_butterfly(Butterfly())

    for c in range(iters):

        butterfly_pop.get_best_butterfly()

        for i in range(pop):
            butterfly_pop.butterfly_pop[i].sniff(stimulus, butterfly_pop.force)
            if random.random() < p:
                butterfly_pop.butterfly_pop[i].move_to_the_best()
            else:
                butterfly_pop.butterfly_pop[i].move()

        butterfly_pop.set_force(c, iters)
