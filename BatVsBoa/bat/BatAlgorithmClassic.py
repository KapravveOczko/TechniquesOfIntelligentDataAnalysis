import random

from bat.BatPop import BatPop
from bat.Bat import Bat


def bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max,
                          alpha, epsilon, iters, dimensions):
    bat_best_results = []
    bat_pop = BatPop(function)

    for i in range(pop_count):
        new_bat = Bat(function_bounds, frequency_min, frequency_max,
                               alpha, epsilon, dimensions)
        new_bat.set_score(function)
        bat_pop.append_bat(new_bat)

    for i in range(iters):
        for bat in bat_pop.bat_pop:
            bat.set_position()
            bat.set_velocity(bat_pop.best_bat_coordinates)
            bat.set_score(function)

        bat_pop.get_average()

        for bat in bat_pop.bat_pop:
            bat.set_position_after_setting_position(bat_pop.average_volume)
            if bat.volume > random.random() and bat.score < bat_pop.best_bat_score:
                bat_pop.best_bat_score = bat.score
                bat_pop.best_bat_coordinates = bat.coordinates
                bat.set_volume()
                bat.set_emission()

        bat_best_results.append(bat_pop.best_bat_score)

    return bat_best_results
