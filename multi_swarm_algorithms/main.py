
from sma.multi_swarm_sma import MS_SMA
from pso.gl_pso import GL_PSO
from localLib.Functions import rosenbrock_function, rosenbrock_bounds
from localLib.drawer_helper import draw_plot_contains_parameter_to_best_score

iterations = 100
num_agents = 100
func = rosenbrock_function
bounds = rosenbrock_bounds
dimensions = 20

# MS_SMA parameters
swarms = 5
w = 0.5
vb = 0.05
z = 0.8

# PSO_Genetic_Learning parameters

c1 = 0.5
c2 = 0.5
w = 0.5
cross_rate = 0.5
mutation_rate = 0.3


ms_sma = MS_SMA(swarms, iterations, num_agents, dimensions, w, vb, z, func, bounds)
best_value_history = ms_sma.run()

# pso_genetic_learning = GL_PSO(num_agents, iterations, dimensions, c1, c2, w, cross_rate, mutation_rate, func, bounds)
# best_value_history = pso_genetic_learning.run()

iterations_tab = [i for i in range(len(best_value_history))]

print('best value: ', best_value_history[-1])

draw_plot_contains_parameter_to_best_score(iterations_tab, best_value_history, 'iterations', 'Best value', 'MS_SMA', 'ms_sma')
# draw_plot_contains_parameter_to_best_score(iterations_tab, best_value_history, 'iterations', 'Best value', 'GL_PSO', 'gl_pso')



