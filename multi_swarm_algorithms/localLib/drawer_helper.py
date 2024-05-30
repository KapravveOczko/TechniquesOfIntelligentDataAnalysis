import matplotlib.pyplot as plt


def generate_parameter_check_tex():
    with open('report_text.tex', 'a', encoding='utf-8') as f:
        pass



def draw_plot_contains_parameter_to_best_score(tab_with_parameters, tab_with_best_score, parameter_name, title, label_name, file_name):
    plt.figure(figsize=(10, 6))
    plt.plot(tab_with_parameters, tab_with_best_score, label=label_name)
    plt.title(title)
    plt.xlabel(parameter_name)
    plt.ylabel('Best Value')
    plt.legend()
    plt.savefig(f'plots/{file_name}')


