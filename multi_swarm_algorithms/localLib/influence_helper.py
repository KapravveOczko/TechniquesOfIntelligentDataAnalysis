
from .drawer_helper import draw_plot_contains_parameter_to_best_score


def generate_single_parameter_check_text(f, parameter_name, algorithm_name, plot_name):
    f.write(r'\subsection{Wpływ ' + parameter_name + ' dla ' + algorithm_name + '}' + '\n\n')
    f.write(r'\begin{figure}[H]' + '\n')
    f.write(r'\centering' + '\n')
    f.write(r'\includegraphics[width=1\textwidth]{plots/' + plot_name + '}' + '\n')
    f.write(r'\caption{Wynik eksperymentu dla ' + parameter_name + ' dla ' + algorithm_name + '}' + '\n')
    f.write(r'\label{fig:' + plot_name + '}' + '\n')
    f.write(r'\end{figure}' + '\n')
    f.write('\n')


def generate_parameter_check_tex():
    with open('report_text.tex', 'a', encoding='utf-8') as f:
        generate_single_parameter_check_text(f, 'populacji', 'pso z algorytmem genetycznym', 'GL_PSO_population.png')
        generate_single_parameter_check_text(f, 'iteracji', 'pso z algorytmem genetycznym', 'GL_PSO_iterations.png')
        generate_single_parameter_check_text(f, 'współczynnika bezwładności', 'pso z algorytmem genetycznym', 'GL_PSO_w.png')
        generate_single_parameter_check_text(f, 'wpływ kognitywny', 'pso z algorytmem genetycznym', 'GL_PSO_c1.png')
        generate_single_parameter_check_text(f, 'wpływ społeczny', 'pso z algorytmem genetycznym', 'GL_PSO_c2.png')
        generate_single_parameter_check_text(f, 'współczynnika mutacji', 'pso z algorytmem genetycznym', 'GL_PSO_mutation_rate.png')
        generate_single_parameter_check_text(f, 'współczynnika krzyżowania', 'pso z algorytmem genetycznym', 'GL_PSO_cross_rate.png')
        generate_single_parameter_check_text(f, 'populacji', 'sztucznej kolonii slimaków', 'MS_SMA_population.png')
        generate_single_parameter_check_text(f, 'iteracji', 'sztucznej kolonii slimaków', 'MS_SMA_iterations.png')
        generate_single_parameter_check_text(f, 'współczynnika bezwładności', 'sztucznej kolonii slimaków', 'MS_SMA_w.png')
        generate_single_parameter_check_text(f, 'współczynnika lokalnego przyspieszenia', 'sztucznej kolonii slimaków', 'MS_SMA_vb.png')
        generate_single_parameter_check_text(f, 'współczynnika globalnego przyspieszenia', 'sztucznej kolonii slimaków', 'MS_SMA_z.png')


def influence_check(parameters, algorithm, checked_parameters, parameter_name, algorithm_name):
    best_results = []

    for parameter in checked_parameters:
        parameters[parameter_name] = parameter
        print(f'{parameter_name}: {parameter}')

        parameters_list = list(parameters.values())

        best_results.append(algorithm(*parameters_list).run()[-1])
        print(f'boa levy done best score: {best_results[-1]}')

    draw_plot_contains_parameter_to_best_score(checked_parameters, best_results, parameter_name, 'best score', algorithm_name, f'{algorithm_name}_{parameter_name}_influence_check')