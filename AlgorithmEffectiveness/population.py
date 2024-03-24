from entity import Entity

import numpy as np


class Population:
    def __init__(self, func, bounds, pop_size=15, max_generations=1000, F=0.5, CR=0.5, dimension=20, with_variants=False):
        self.func = func
        self.bounds = bounds
        self.pop_size = pop_size
        self.max_generations = max_generations
        self.F = F
        self.CR = CR
        self.dimension = dimension
        self.with_variants = with_variants
        self.population = [Entity(coordinates, self.func) for coordinates in np.random.uniform(low=bounds[0], high=bounds[1], size=(pop_size, dimension))]
        self.best_individual = self.population[np.argmin([ind.value for ind in self.population])]
        self.best_values_list = [self.best_individual.value]

    def calculate_best_value(self):
        for _ in range(self.max_generations):
            for i in range(self.pop_size):
                # Mutation
                mutant = self.get_mutant()

                # Crossover
                trial = self.get_trial(i, mutant)

                # Selection
                if trial.value < self.population[i].value:
                    self.population[i] = trial
                    if self.best_individual.value > trial.value:
                        self.best_individual = trial
            self.best_values_list.append(self.best_individual.value)

        return self.best_individual.coordinates, self.best_individual.value, self.best_values_list

    def get_mutant(self):
        a, b, c = np.random.choice(self.pop_size, 3, replace=False)
        b_minus_c = self.population[b].coordinates - self.population[c].coordinates
        if self.with_variants:
            mutant = self.best_individual.coordinates + self.F * (self.population[a].coordinates - self.best_individual.coordinates + b_minus_c)
        else:
            mutant = self.population[a].coordinates + self.F * (b_minus_c)
        return mutant

    def get_trial(self, i, mutant):
        trial = np.copy(self.population[i].coordinates)
        j_rand = np.random.randint(self.dimension)
        for j in range(self.dimension):
            if np.random.rand() < self.CR or j == j_rand:
                trial[j] = mutant[j]
        return Entity(trial, self.func)

