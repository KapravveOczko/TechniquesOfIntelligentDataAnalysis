
from sma.multi_swarm_sma import MS_SMA
from pso.gl_pso import GL_PSO
from localLib.Functions import *
from localLib.drawer_helper import draw_plot_contains_parameter_to_best_score
from localLib.influence_helper import influence_check, generate_parameter_check_tex

iterations = 1000
population = 100
func = sphere_function
bounds = sphere_bounds
dimensions = 20



# MS_SMA parameters
swarms = 5
sma_w = 0.5
vb = 0.05
z = 0.8

ms_sma_parameters = {
    'swarms': swarms,
    'iterations': iterations,
    'population': population,
    'dimensions': dimensions,
    'w': sma_w,
    'vb': vb,
    'z': z,
    'func': func,
    'bounds': bounds
}

# PSO_Genetic_Learning parameters
c1 = 0.5
c2 = 0.5
pso_w = 0.5
cross_rate = 0.5
mutation_rate = 0.3

pso_genetic_learning_parameters = {
    'population': population,
    'iterations': iterations,
    'dimensions': dimensions,
    'c1': c1,
    'c2': c2,
    'w': pso_w,
    'cross_rate': cross_rate,
    'mutation_rate': mutation_rate,
    'func': func,
    'bounds': bounds
}


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
        f.write(r'Rozmiar populacji & ' + str(population) + r' \\' + '\n')
        f.write(r'Maksymalna liczba generacji & ' + str(iterations) + r' \\' + '\n')
        f.write(r'Wymiar & ' + str(dimensions) + r' \\' + '\n')
        f.write(r'Funkcja & ' + str(func) + r' \\' + '\n')
        f.write(r'pso w & ' + str(pso_w) + r' \\' + '\n')
        f.write(r'pso c1 & ' + str(c1) + r' \\' + '\n')
        f.write(r'pso c2 & ' + str(c2) + r' \\' + '\n')
        f.write(r'pso cross rate & ' + str(cross_rate) + r' \\' + '\n')
        f.write(r'pso mutation rate & ' + str(mutation_rate) + r' \\' + '\n')
        f.write(r'sma w & ' + str(sma_w) + r' \\' + '\n')
        f.write(r'sma vb & ' + str(vb) + r' \\' + '\n')
        f.write(r'sma z & ' + str(z) + r' \\' + '\n')
        f.write(r'sma swarms & ' + str(swarms) + r' \\' + '\n')
        f.write(r'\hline' + '\n')
        f.write(r'\end{tabular}' + '\n')
        f.write(r'\end{table}' + '\n')
        f.write('\n')
        f.write(r'\subsection{Dobór parametrów}' + '\n\n')
        f.write(r'W tej sekcji badaniu poddane zostaną parametry wejściowe obu algorytmów oraz ich wpływ na ostateczny wynik, w tym celu posłużymy się manipulacjami na funkcji Rastring, jej wolny spadek pozwoli dokładniej zobrazować wpływ wprowadzonych zmian.' + '\n\n')

    generate_parameter_check_tex()



generate_text_in_tex()

# influence_check(pso_genetic_learning_parameters, GL_PSO, [100, 300, 500, 700, 900], 'iterations', 'GL_PSO')
# influence_check(pso_genetic_learning_parameters, GL_PSO, [50, 100, 150, 200, 250], 'population', 'GL_PSO')
# influence_check(pso_genetic_learning_parameters, GL_PSO, [0.1, 0.3, 0.5, 0.7, 0.9], 'w', 'GL_PSO')
# influence_check(pso_genetic_learning_parameters, GL_PSO, [0.1, 0.3, 0.5, 0.7, 0.9], 'c1', 'GL_PSO')
# influence_check(pso_genetic_learning_parameters, GL_PSO, [0.1, 0.3, 0.5, 0.7, 0.9], 'c2', 'GL_PSO')
# influence_check(pso_genetic_learning_parameters, GL_PSO, [0.1, 0.3, 0.5, 0.7, 0.9], 'cross_rate', 'GL_PSO')
# influence_check(pso_genetic_learning_parameters, GL_PSO, [0.1, 0.3, 0.5, 0.7, 0.9], 'mutation_rate', 'GL_PSO')

# influence_check(ms_sma_parameters, MS_SMA, [2, 4, 6, 8, 10], 'swarms', 'MS_SMA')
# influence_check(ms_sma_parameters, MS_SMA, [100, 300, 500, 700, 900], 'iterations', 'MS_SMA')
# influence_check(ms_sma_parameters, MS_SMA, [50, 100, 150, 200, 250], 'population', 'MS_SMA')
# influence_check(ms_sma_parameters, MS_SMA, [0.1, 0.3, 0.5, 0.7, 0.9], 'w', 'MS_SMA')
# influence_check(ms_sma_parameters, MS_SMA, [0.01, 0.03, 0.05, 0.07, 0.09], 'vb', 'MS_SMA')
# influence_check(ms_sma_parameters, MS_SMA, [0.1, 0.3, 0.5, 0.7, 0.9], 'z', 'MS_SMA')



# # MS_SMA algorithm

ms_sma = MS_SMA(swarms, iterations, population, dimensions, sma_w, vb, z, func, bounds)
best_value_history = ms_sma.run()

iterations_tab = [i for i in range(len(best_value_history))]

print('best value: ', best_value_history[-1])

draw_plot_contains_parameter_to_best_score(iterations_tab, best_value_history, 'iterations', 'Best value', 'MS_SMA', 'ms_sma')





# # GL_PSO algorithm

# pso_genetic_learning = GL_PSO(population, iterations, dimensions, c1, c2, pso_w, cross_rate, mutation_rate, func, bounds)
# best_value_history = pso_genetic_learning.run()

# iterations_tab = [i for i in range(len(best_value_history))]

# print('best value: ', best_value_history[-1])
# draw_plot_contains_parameter_to_best_score(iterations_tab, best_value_history, 'iterations', 'Best value', 'GL_PSO', 'gl_pso')

