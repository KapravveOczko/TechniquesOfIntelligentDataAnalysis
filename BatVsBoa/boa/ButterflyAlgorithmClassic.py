import random
from boa.ButterflyPop import ButterflyPop
from boa.Butterfly import Butterfly

import numpy as np


def butterfly_algorithm_classic(iters, pop_count, function, function_bounds, p=0.8, dimensions=20):
    butterfly_pop = ButterflyPop(function)
    boa_best_results = []

    boa_best_score = np.inf
    boa_best_coordinates = np.zeros(dimensions)

    for i in range(pop_count):
        new_butterfly = Butterfly(function_bounds, dimensions)
        new_butterfly.calculate_score(function)
        butterfly_pop.append_butterfly(new_butterfly)
        if new_butterfly.score < boa_best_score:
            boa_best_score = new_butterfly.score
            boa_best_coordinates = new_butterfly.coordinates

    boa_best_results.append(boa_best_score)

    for c in range(iters):

        for i in range(pop_count):
            r = random.random()
            butterfly_pop.butterfly_pop[i].sniff(random.random(), butterfly_pop.force)
            if r < p:
                butterfly_pop.butterfly_pop[i].move_to_the_best(r, boa_best_coordinates)
            else:
                butterfly_pop.butterfly_pop[i].move(r, butterfly_pop.random_insects())

        butterfly_pop.set_force(c, iters)

        for i in range(pop_count):
            new_butterfly = Butterfly(function_bounds, dimensions)
            new_butterfly.calculate_score(function)
            butterfly_pop.append_butterfly(new_butterfly)
            if new_butterfly.score < boa_best_score:
                boa_best_score = new_butterfly.score
                boa_best_coordinates = new_butterfly.coordinates

        boa_best_results.append(boa_best_score)

    return boa_best_results
