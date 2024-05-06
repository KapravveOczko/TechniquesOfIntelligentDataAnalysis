from bat.BatAlgorithmClassic import bat_algorithm_classic
from boa.ButterflyAlgorithmClassic import butterfly_algorithm_classic
from boa.ButterflyAlgorithmLevy import butterfly_algorithm_levy
from localLib.Printer import print_bat_vs_boa
from localLib.Functions import *

from localLib.drawer_helper import draw_plot_contains_parameter_to_best_score, generate_parameter_check_tex
import matplotlib.pyplot as plt


# all
pop_count = 400
iters = 1500
function = rastrigin_function
function_bounds = rastrigin_bounds
dimensions = 20
# bat
frequency_min = 0
frequency_max = 1
alpha = 0.5
epsilon = 0.5
# boa
p = 0.8
# boa levy
alpha_levy = 1.5

def alpha_levy_influence_check():
    alpha_levy_list_to_check = [1, 1.5, 2]

    boa_levy_best_results = []

    for alpha_levy in alpha_levy_list_to_check:
        print(f'Alpha levy: {alpha_levy}')
        boa_levy_best_results.append(butterfly_algorithm_levy(iters, pop_count, function, function_bounds, alpha_levy, p, dimensions)[-1])
        print(f'boa levy done best score: {boa_levy_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(alpha_levy_list_to_check, boa_levy_best_results, 'Alpha levy', 'best score', 'BOA-levy', 'boa_levy_alpha')

def epsilon_influence_check():
    epsilon_list_to_check = [0.1, 0.3, 0.6, 0.8]

    bat_best_results = []

    for eps in epsilon_list_to_check:
        print(f'Epsilon: {eps}')
        bat_best_results.append(bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, eps, iters, dimensions)[-1])
        print(f'bat done best score: {bat_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(epsilon_list_to_check, bat_best_results, 'Epsilon', 'best score', 'BAT', 'bat_epsilon')

def alpha_influence_check():
    alpha_list_to_check = [0.1, 0.3, 0.6, 0.8]

    bat_best_results = []

    for alpha in alpha_list_to_check:
        print(f'Alpha: {alpha}')
        bat_best_results.append(bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, epsilon, iters, dimensions)[-1])
        print(f'bat done best score: {bat_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(alpha_list_to_check, bat_best_results, 'Alpha', 'best score', 'BAT', 'bat_alpha')

def frequency_influence_check():
    frequency_list_to_check = [1, 2, 5]

    bat_best_results = []

    for freq in frequency_list_to_check:
        print(f'Frequency: [{frequency_min}, {freq}]')
        bat_best_results.append(bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, freq, alpha, epsilon, iters, dimensions)[-1])
        print(f'bat done best score: {bat_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(frequency_list_to_check, bat_best_results, 'Frequency', 'best score', 'BAT', 'bat_frequency')

def dimensions_influence_check():
    dimensions_list_to_check = [20, 25, 30]

    bat_best_results = []
    boa_levy_best_results = []

    for dim in dimensions_list_to_check:
        print(f'Dimensions: {dim}')
        bat_best_results.append(bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, epsilon, iters, dim)[-1])
        print(f'bat done best score: {bat_best_results[-1]}')
        boa_levy_best_results.append(butterfly_algorithm_levy(iters, pop_count, function, function_bounds, alpha_levy, p, dim)[-1])
        print(f'boa levy done best score: {boa_levy_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(dimensions_list_to_check, bat_best_results, 'Dimensions', 'best score', 'BAT', 'bat_dimensions')
    draw_plot_contains_parameter_to_best_score(dimensions_list_to_check, boa_levy_best_results, 'Dimensions', 'best score', 'BOA-levy', 'boa_levy_dimensions')

def iterations_influence_check():
    iterations_list_to_check = [1000, 1500, 2000, 2500, 3000]

    bat_best_results = []
    boa_levy_best_results = []

    for iters_count in iterations_list_to_check:
        print(f'Iterations: {iters_count}')
        bat_best_results.append(bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, epsilon, iters_count, dimensions)[-1])
        print(f'bat done best score: {bat_best_results[-1]}')
        boa_levy_best_results.append(butterfly_algorithm_levy(iters_count, pop_count, function, function_bounds, alpha_levy, p, dimensions)[-1])
        print(f'boa levy done best score: {boa_levy_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(iterations_list_to_check, bat_best_results, 'Iterations', 'best score', 'BAT', 'bat_iterations')
    draw_plot_contains_parameter_to_best_score(iterations_list_to_check, boa_levy_best_results, 'Iterations', 'best score', 'BOA-levy', 'boa_levy_iterations')


def population_influence_check():
    population_list_to_check = [50, 100, 200, 400, 600]

    bat_best_results = []
    boa_levy_best_results = []

    for pop_count in population_list_to_check:
        print(f'Population: {pop_count}')
        bat_best_results.append(bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, epsilon, iters, dimensions)[-1])
        print(f'bat done best score: {bat_best_results[-1]}')
        boa_levy_best_results.append(butterfly_algorithm_levy(iters, pop_count, function, function_bounds, alpha_levy, p, dimensions)[-1])
        print(f'boa levy done best score: {boa_levy_best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(population_list_to_check, bat_best_results, 'Population', 'best score', 'BAT', 'bat_population')
    draw_plot_contains_parameter_to_best_score(population_list_to_check, boa_levy_best_results, 'Population', 'best score', 'BOA-levy', 'boa_levy_population')


def generate_text_in_tex():
    with open('report_text.tex', 'w', encoding='utf-8') as f:
        f.write(r'\subsection{Parametry początkowe używane do badania wpływu parametrów}' + '\n\n')
        f.write(r'\begin{table}[htbp]' + '\n')
        f.write(r'\centering' + '\n')
        f.write(r'\caption{Parametry początkowe algorytmu}' + '\n')
        f.write(r'\label{tab:params}' + '\n')
        f.write(r'\begin{tabular}{|c|c|}' + '\n')
        f.write(r'\hline' + '\n')
        f.write(r'Parametr & Wartość \\' + '\n')
        f.write(r'\hline' + '\n')
        f.write(r'Rozmiar populacji & ' + str(pop_count) + r' \\' + '\n')
        f.write(r'Maksymalna liczba generacji & ' + str(iters) + r' \\' + '\n')
        f.write(r'Wymiar & ' + str(dimensions) + r' \\' + '\n')
        f.write(r'Minimalna częstotliwość & ' + str(frequency_min) + r' \\' + '\n')
        f.write(r'Maksymalna częstotliwość & ' + str(frequency_max) + r' \\' + '\n')
        f.write(r'Alpha & ' + str(alpha) + r' \\' + '\n')
        f.write(r'Epsilon & ' + str(epsilon) + r' \\' + '\n')
        f.write(r'Alpha levy & ' + str(alpha_levy) + r' \\' + '\n')
        f.write(r'\hline' + '\n')
        f.write(r'\end{tabular}' + '\n')
        f.write(r'\end{table}' + '\n')
        f.write('\n')
        f.write(r'\subsection{Dobór parametrów}' + '\n\n')
        f.write(r'W tej sekcji badaniu poddane zostaną parametry wejściowe obu algorytmów oraz ich wpływ na ostateczny wynik, w tym celu posłużymy się manipulacjami na funkcji Rastring, jej wolny spadek pozwoli dokładniej zobrazować wpływ wprowadzonych zmian.' + '\n\n')

    generate_parameter_check_tex()

if __name__ == "__main__":


    generate_text_in_tex()

    # population_influence_check()
    # iterations_influence_check()
    # dimensions_influence_check()
    # frequency_influence_check()
    # alpha_influence_check()
    # epsilon_influence_check()
    # alpha_levy_influence_check()












    # bat_best_results = bat_algorithm_classic(pop_count, function, function_bounds, frequency_min, frequency_max, alpha, epsilon, iters, dimensions)

    # boa_best_results = butterfly_algorithm_classic(iters, pop_count, function, function_bounds, p, dimensions)

    # boa_levy_best_results = butterfly_algorithm_levy(iters, pop_count, function, function_bounds, alpha_levy, p, dimensions)

    # print(f"Best BAT: {bat_best_results[-1]}")
    # print(f"Best BOA classic: {boa_best_results[-1]}")
    # print(f"Best BOA levy: {boa_levy_best_results[-1]}")

    # plt.figure(figsize=(10, 6))
    # plt.plot(bat_best_results, label='BAT')
    # plt.plot(boa_best_results, label='BOA')
    # plt.plot(boa_levy_best_results, label='BOA-levy')
    # plt.xlabel('Generation')
    # plt.ylabel('Best Value')
    # plt.legend()
    # plt.show()
