from entity import Entity

import numpy as np

class PSO_DE:
    def __init__(self, func, bounds, pop_size=15, max_generations=1000, w=0.5, c1=0.5, c2=0.5, dimension=20, with_variants=False):
        self.func = func
        self.bounds = bounds
        self.pop_size = pop_size
        self.max_generations = max_generations
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.dimension = dimension
        self.with_variants = with_variants
        self.population = [Entity(coordinates, self.func) for coordinates in np.random.uniform(low=bounds[0], high=bounds[1], size=(pop_size, dimension))]
        self.velocities = np.random.rand(pop_size, dimension)
        self.best_individual = self.population[np.argmin([ind.value for ind in self.population])]
        self.best_values_list = [self.best_individual.value]

    def calculate_best_value(self):
        for _ in range(self.max_generations):
            for j in range(self.pop_size):
                self.velocities[j] = self.w * self.velocities[j] + self.c1 * np.random.rand() * (self.population[j].best_coordinates - self.population[j].coordinates) + self.c2 * np.random.rand() * (self.best_individual.coordinates - self.population[j].coordinates)
                self.population[j].coordinates += self.velocities[j]
                self.population[j].calculate_best_value()

            for i in range(self.pop_size):

                a, b, c = np.random.choice(self.pop_size, 3, replace=False)
                a_minus_b = self.population[a].coordinates - self.population[b].coordinates

                new_position = self.population[i].coordinates + np.random.rand() * a_minus_b + np.random.rand() * (self.best_individual.coordinates - self.population[c].coordinates)

                new_entity = Entity(new_position, self.func)

                if new_entity.value < self.population[i].value:
                    self.population[i] = new_entity

                    if new_entity.value < self.best_individual.value:
                        self.best_individual = new_entity
            self.best_values_list.append(self.best_individual.value)

        return self.best_individual.coordinates, self.best_individual.value, self.best_values_list
