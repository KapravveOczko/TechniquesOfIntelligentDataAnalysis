import random

from BatPop import BatPop
from Bat import Bat


def bat_algorithm_classic(pop_count, function, function_bounds_min, function_bounds_max, frequency_min, frequency_max,
                          alpha, epsilon, iters):

    bat_pop = BatPop(function)

    for i in range(pop_count):
        bat_pop.append_bat(Bat(random.uniform(function_bounds_min, function_bounds_max), frequency_min, frequency_max,
                               alpha, epsilon))

    for i in range(iters):
        for bat in bat_pop.bat_pop:
            bat.set_position()
            bat.set_velocity()
        bat_pop.get_average()
        for bat in bat_pop.bat_pop:
            bat.set_position_after_setting_position(bat_pop.average_volume)
            bat.set_volume()
            bat.set_frequency()
        bat_pop.set_best_bat_x()

    return bat_pop.best_bat_x, bat_pop.function(bat_pop.best_bat_x)
