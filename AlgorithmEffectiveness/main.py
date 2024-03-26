from differential_evolution import Different_Evolution
from pso_with_differential_evolution import PSO_DE
from functions import rastrigin_function, rastrigin_bounds, rosenbrock_function, rosenbrock_bounds, sphere_function, sphere_bounds, griewank_function, griewank_bounds
import matplotlib.pyplot as plt

function = rosenbrock_function
bounds = rosenbrock_bounds
pop_size = 50
max_generations = 1000
F = 0.8
CR = 0.8
dimension = 20

if __name__ == "__main__":
    print()
    print("different evaluations with variant 6")
    different_evolution = Different_Evolution(function, bounds, pop_size, max_generations, F, CR, dimension, True)
    best_solution, best_value, best_values_list_with_variants = different_evolution.calculate_best_value()
    print(f"DE with variant 6 Best value: {best_value} for {dimension} dimensions")

    print()
    print("PSO with different evaluations")

    pso_de = PSO_DE(function, bounds, pop_size, max_generations, dimension=dimension)

    best_solution, best_value, best_values_list_without_variants = pso_de.calculate_best_value()
    print(f"PSO-DE Best value: {best_value} for {dimension} dimensions")


    plt.figure(figsize=(10, 6))
    plt.plot(best_values_list_without_variants, label='PSO+DE')
    plt.plot(best_values_list_with_variants, label='DE with variant 6')
    plt.xlabel('Generation')
    plt.ylabel('Best Value')
    plt.legend()
    plt.show()