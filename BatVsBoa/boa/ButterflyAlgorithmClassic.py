import random
from boa.ButterflyPop import ButterflyPop
from boa.Butterfly import Butterfly


def butterfly_algorithm_classic(iters, pop_count, function, p=0.8):
    butterfly_pop = ButterflyPop(function)
    best_x_for_printer = []
    best_value_for_printer = []

    for i in range(pop_count):
        butterfly_pop.append_butterfly(Butterfly())

    for c in range(iters):
        r = random.random()
        butterfly_pop.get_best_butterfly()

        for i in range(pop_count):
            butterfly_pop.butterfly_pop[i].sniff(butterfly_pop.get_stimulus(i), butterfly_pop.force)
            if r < p:
                butterfly_pop.butterfly_pop[i].move_to_the_best(r, butterfly_pop.best_butterfly_value)
            else:
                butterfly_pop.butterfly_pop[i].move(r, butterfly_pop.random_insects())

        butterfly_pop.set_force(c, iters)

        best_x_for_printer.append(butterfly_pop.best_butterfly)
        best_value_for_printer.append(butterfly_pop.best_butterfly_value)

    return butterfly_pop.best_butterfly, butterfly_pop.best_butterfly_value, best_x_for_printer, best_value_for_printer
