import numpy as np

rosenbrock_bounds = [-2.048, 2.048]
rastrigin_bounds = [-5.12, 5.12]

def rastrigin_function(x):
    n = len(x)
    sum_values = 0
    for i in range(n):
        sum_values += x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 10
    return sum_values

def rosenbrock_function(x):
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)