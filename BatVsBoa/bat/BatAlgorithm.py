import numpy as np

class BatAlgorithm:
    def __init__(self, population_size, num_generations, loudness, pulse_rate, min_frequency, max_frequency, lower_bound, upper_bound, objective_function, dimensions):
        self.dimensions = dimensions
        self.population_size = population_size
        self.num_generations = num_generations
        self.loudness = loudness
        self.pulse_rate = pulse_rate
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.objective_function = objective_function
        self.bat_best_results = []

    def initialize_bats(self):
        velocity = np.zeros((self.population_size, self.dimensions))
        frequency = np.zeros(self.population_size)
        for i in range(self.population_size):
            frequency[i] = np.random.uniform(self.min_frequency, self.max_frequency)
        return velocity, frequency

    def apply_bounds(self, solution):
        return np.clip(solution, self.lower_bound, self.upper_bound)

    def bat_algorithm(self):
        solutions = np.random.uniform(self.lower_bound, self.upper_bound, (self.population_size, self.dimensions))
        velocity, frequency = self.initialize_bats()
        best_fitness = float("inf")
        best_solution = solutions[0]
        for i in range(self.population_size):
            fitness = self.objective_function(solutions[i])
            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = solutions[i]

        self.bat_best_results.append(best_fitness)
        for t in range(self.num_generations):
            for i in range(self.population_size):
                frequency[i] = self.min_frequency + (self.max_frequency - self.min_frequency) * np.random.uniform(0, 1)
                velocity[i] = velocity[i] + (solutions[i] - best_solution) * frequency[i]
                solutions[i] = self.apply_bounds(solutions[i] + velocity[i])
                if np.random.uniform(0, 1) > self.pulse_rate:
                    solutions[i] = self.apply_bounds(best_solution + 0.001 * np.random.randn(self.dimensions))
                new_fitness = self.objective_function(solutions[i])
                if (new_fitness <= best_fitness) and (np.random.uniform(0, 1) < self.loudness):
                    best_fitness = new_fitness
                    best_solution = solutions[i]
            self.bat_best_results.append(best_fitness)
        return self.bat_best_results
