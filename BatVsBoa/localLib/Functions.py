import numpy as np

rosenbrock_bounds = {'min': -2.048, 'max': 2.048}
rastrigin_bounds = {'min': -5.12, 'max': 5.12}
sphere_bounds = {'min': -100, 'max': 100}
griewank_bounds = {'min': -600, 'max': 600}

def rastrigin_function(x):
    n = len(x)
    sum_values = 0
    for i in range(n):
        sum_values += x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i]) + 10
    return sum_values


def rosenbrock_function(x):
    return np.sum(100.0 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)


def sphere_function(x):
    return np.sum(x[i] ** 2 for i in range(len(x)))


def griewank_function(x):
    n = len(x)

    sum_term = np.sum(np.square(x) / 4000)
    product_term = np.prod(np.cos(np.array(x) / np.sqrt(range(1, n + 1))))

    return 1 + sum_term - product_term
