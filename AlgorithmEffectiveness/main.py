from population import Population
from functions import rastrigin_function, rastrigin_bounds, rosenbrock_function, rosenbrock_bounds, sphere_function, sphere_bounds, griewank_function, griewank_bounds
import matplotlib.pyplot as plt

function = rosenbrock_function
bounds = rosenbrock_bounds
pop_size = 20
max_generations = 3000
F = 0.8
CR = 0.8
dimension = 20

if __name__ == "__main__":
    print()
    print("different evaluations")
    population = Population(function, bounds, pop_size, max_generations, F, CR, dimension)
    best_solution, best_value, best_values_list_without_variants = population.calculate_best_value()
    print(f"Best value: {best_value} for {dimension} dimensions")

    print()
    print("different evaluations with variant 6")
    population = Population(function, bounds, pop_size, max_generations, F, CR, dimension, True)
    best_solution, best_value, best_values_list_with_variants = population.calculate_best_value()
    print(f"Best value: {best_value} for {dimension} dimensions")

    plt.figure(figsize=(10, 6))
    plt.plot(best_values_list_without_variants, label='Without Variants')
    plt.plot(best_values_list_with_variants, label='With Variants')
    plt.xlabel('Generation')
    plt.ylabel('Best Value')
    plt.legend()
    plt.show()