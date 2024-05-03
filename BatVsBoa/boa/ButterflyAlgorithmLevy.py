import random
from boa.ButterflyPop import ButterflyPop
from boa.Butterfly import Butterfly
from boa.Levy import levy_flight

import numpy as np


def butterfly_algorithm_levy(iters, pop_count, function, function_bounds, alpha, p=0.8, dimensions=20):
    butterfly_pop = ButterflyPop(function)
    boa_best_results = []

    boa_best_score = np.inf
    boa_best_coordinates = np.zeros(dimensions)

    for i in range(pop_count):
        new_butterfly = Butterfly(function_bounds, dimensions)
        new_butterfly.calculate_score(function)
        butterfly_pop.append_butterfly(Butterfly(function_bounds, dimensions))
        if new_butterfly.score < boa_best_score:
            boa_best_score = new_butterfly.score
            boa_best_coordinates = new_butterfly.coordinates

    boa_best_results.append(boa_best_score)

    for c in range(iters):

        for i in range(pop_count):
            new_butterfly = Butterfly(function_bounds, dimensions)
            new_butterfly.calculate_score(function)
            butterfly_pop.append_butterfly(Butterfly(function_bounds, dimensions))
            if new_butterfly.score < boa_best_score:
                boa_best_score = new_butterfly.score
                boa_best_coordinates = new_butterfly.coordinates

        levy = levy_flight(alpha, dimensions)

        for i in range(pop_count):
            butterfly_pop.butterfly_pop[i].sniff(random.random(), butterfly_pop.force)
            if random.random() < p:
                butterfly_pop.butterfly_pop[i].move_to_the_best_levy_style(levy, boa_best_coordinates)
            else:
                butterfly_pop.butterfly_pop[i].move(levy, butterfly_pop.random_insects())

        butterfly_pop.set_force(c, iters)

        boa_best_results.append(boa_best_score)

    return boa_best_results
