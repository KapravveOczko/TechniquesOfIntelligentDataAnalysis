from bat.BatAlgorithmClassic import bat_algorithm_classic
from boa.ButterflyAlgorithmClassic import butterfly_algorithm_classic
from boa.ButterflyAlgorithmLevy import butterfly_algorithm_levy
from localLib.Printer import print_bat_vs_boa
from localLib.Functions import *

from bat.BatAlgorithm import BatAlgorithm
import matplotlib.pyplot as plt


# all
pop_count = 100
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

if __name__ == "__main__":
    bat_best_results = bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, epsilon, iters, dimensions)

    boa_best_results = butterfly_algorithm_classic(iters, pop_count, function, function_bounds, p, dimensions)

    boa_levy_best_results = butterfly_algorithm_levy(iters, pop_count, function, function_bounds, alpha_levy, p, dimensions)

    print(f"Best BAT: {bat_best_results[-1]}")
    print(f"Best BOA classic: {boa_best_results[-1]}")
    print(f"Best BOA levy: {boa_levy_best_results[-1]}")

    plt.figure(figsize=(10, 6))
    plt.plot(bat_best_results, label='BAT')
    plt.plot(boa_best_results, label='BOA')
    plt.plot(boa_levy_best_results, label='BOA-levy')
    plt.xlabel('Generation')
    plt.ylabel('Best Value')
    plt.legend()
    plt.show()

