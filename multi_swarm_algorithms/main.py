
from sma.slime_mould_algorithm import SMA
from localLib.Functions import rosenbrock_function, rosenbrock_bounds
from localLib.drawer_helper import draw_plot_contains_parameter_to_best_score

iterations = 100
num_agents = 100
dimensions = 20
w = 0.5
vb = 0.05
z = 0.7
func = rosenbrock_function
bounds = rosenbrock_bounds


sma = SMA(iterations, num_agents, dimensions, w, vb, z, func, bounds)

best_value_history = sma.run()

iterations_tab = [i for i in range(iterations+1)]

print('best value: ', best_value_history[-1])

draw_plot_contains_parameter_to_best_score(iterations_tab, best_value_history, 'iterations', 'Best value', 'SMA', 'sma')



