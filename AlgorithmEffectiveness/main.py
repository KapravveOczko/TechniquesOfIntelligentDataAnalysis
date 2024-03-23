from population import Population
from functions import rastrigin_function, rastrigin_bounds, rosenbrock_function, rosenbrock_bounds

function = rosenbrock_function
bounds = rosenbrock_bounds
pop_size = 15
max_generations = 1000
F = 0.8
CR = 0.8
dimension = 20

if __name__ == "__main__":
    print()
    print("different evaluations")
    population = Population(function, bounds, pop_size, max_generations, F, CR, dimension)
    best_solution, best_value = population.calculate_best_value()
    print(f"Best value: {best_value} for {dimension} dimensions")

    print()
    print("different evaluations with variant 6")
    population = Population(function, bounds, pop_size, max_generations, F, CR, dimension, True)
    best_solution, best_value = population.calculate_best_value()
    print(f"Best value: {best_value} for {dimension} dimensions")