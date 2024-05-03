from bat.BatAlgorithmClassic import bat_algorithm_classic
from boa.ButterflyAlgorithmClassic import butterfly_algorithm_classic
from boa.ButterflyAlgorithmLevy import butterfly_algorithm_levy
from localLib.Printer import print_bat_vs_boa
from localLib.Functions import *

from bat.BatAlgorithm import BatAlgorithm
import matplotlib.pyplot as plt


# all
pop_count = 500
iters = 1000
function = rastrigin_function
function_bounds = rastrigin_bounds
dimensions = 20
# bat
frequency_min = 0
frequency_max = 1
alpha = 0.5
epsilon = 0.5
# boa, epsilon
p = 0.8
# boa levy
alpha_levy = 150
size_levy = 100

if __name__ == "__main__":
    bat_best_results = bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max,
                                                                   alpha, epsilon, iters, dimensions)
    # bat_best_results = BatAlgorithm(pop_count, iters, alpha, epsilon, frequency_min, frequency_max, function_bounds['min'], function_bounds['max'], function, dimensions).bat_algorithm()

    # boa_best, boa_best_value, boa_x, boa_y = butterfly_algorithm_classic(iters, pop_count, function, p)

    # boa_levy_best, boa_levy_best_value, boa_levy_x, boa_levy_y = butterfly_algorithm_levy(iters, pop_count, function,
    #                                                                                       alpha_levy, size_levy, p)

    print(f"Best BAT: {bat_best_results[-1]}")
    # print("Best BOA classic: ( ", boa_best, " , ", boa_best_value, " )")
    # print("Best BOA levy: ( ", boa_levy_best, " , ", boa_levy_best_value, " )")
    # print_bat_vs_boa(bat_x, bat_y, boa_x, boa_y, boa_levy_x, boa_levy_y)


    plt.figure(figsize=(10, 6))
    plt.plot(bat_best_results, label='BAT')
    plt.xlabel('Generation')
    plt.ylabel('Best Value')
    plt.legend()
    plt.show()

