from bat.BatAlgorithmClassic import bat_algorithm_classic
from boa.ButterflyAlgorithmClassic import butterfly_algorithm_classic
from boa.ButterflyAlgorithmLevy import butterfly_algorithm_levy
from localLib.Printer import print_bat_vs_boa
from localLib.Functions import *

# all
pop_count = 1000
iters = 1000
function = sphere_function
# bat
function_bounds_min, function_bounds_max = sphere_bounds
frequency_min = 0.2
frequency_max = 0.8
alpha = 0.2
epsilon = 0.05
# boa
p = 0.8
# boa levy
alpha_levy = 150
size_levy = 100

if __name__ == "__main__":
    bat_best, bat_best_value, bat_x, bat_y = bat_algorithm_classic(pop_count, function, function_bounds_min,
                                                                   function_bounds_max, frequency_min, frequency_max,
                                                                   alpha, epsilon, iters)

    boa_best, boa_best_value, boa_x, boa_y = butterfly_algorithm_classic(iters, pop_count, function, p)

    boa_levy_best, boa_levy_best_value, boa_levy_x, boa_levy_y = butterfly_algorithm_levy(iters, pop_count, function,
                                                                                          alpha_levy, size_levy, p)

    print("Best BAT: ( ", bat_best, " , ", bat_best_value, " )")
    print("Best BOA classic: ( ", boa_best, " , ", boa_best_value, " )")
    print("Best BOA levy: ( ", boa_levy_best, " , ", boa_levy_best_value, " )")
    print_bat_vs_boa(bat_x, bat_y, boa_x, boa_y, boa_levy_x, boa_levy_y)
