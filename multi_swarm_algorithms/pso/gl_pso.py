from .entity import Entity
import numpy as np

class GL_PSO:
    def __init__(self, population_size, iterations, dimensions, c1, c2, w, cross_rate, mutation_rate, func, bounds):
        self.population_size = population_size
        self.iterations = iterations
        self.dimensions = dimensions
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.cross_rate = cross_rate
        self.mutation_rate = mutation_rate
        self.func = func
        self.bounds = bounds
        self.best_value = float('inf')
        self.best_position = None
        self.population = []

        for _ in range(population_size):
            entity = Entity(dimensions, func, bounds)
            self.population.append(entity)

            if entity.best_value < self.best_value:
                self.best_value = entity.best_value
                self.best_position = entity.best_position

        self.best_value_history = [self.best_value]

    def run(self):
        for _ in range(self.iterations):           
            for entity in self.population:
                entity.calculate_new_position()

                if entity.best_value < self.best_value:
                    self.best_value = entity.best_value
                    self.best_position = np.copy(entity.best_position)

            for particle in self.population:
                if np.random.rand() < self.cross_rate:
                    partner = np.random.choice(self.population)
                    if particle.best_value > partner.best_value:
                        particle.position = partner.best_position - particle.position
                    else:
                        particle.position = particle.position - partner.best_position

                if np.random.rand() < self.mutation_rate:
                    particle.position = np.random.uniform(self.bounds['min'], self.bounds['max'], self.dimensions)

                particle.update_velocity(self.best_position, self.c1, self.c2, self.w)
                particle.update_position()

                if particle.best_value < self.best_value:
                    self.best_value = particle.best_value
                    self.best_position = np.copy(particle.best_position)

            self.best_value_history.append(self.best_value)

        return self.best_value_history