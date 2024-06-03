
import numpy as np

from .entity import Entity

class SMA:

    def __init__(self, iterations, num_agents, dimensions, w, vb, z, func, bounds):

        self.iterations = iterations
        self.num_agents = num_agents
        self.dimensions = dimensions
        self.w = w
        self.vb = vb
        self.z = z
        self.func = func
        self.bounds = bounds

        positions = np.random.uniform(bounds['min'], bounds['max'], size=(num_agents, dimensions))
        self.population = [Entity(position, func) for position in positions]

        self.population.sort(key=lambda x: x.value)

        self.best_value = self.population[0].value
        self.best_position = self.population[0].position

        self.best_value_history = [self.best_value]


    def run(self):
        for i in range(self.iterations):
            self.update_weights(i)
            self.update_positions()
            self.best_value_history.append(self.best_value)

        return self.best_value_history

    def run_by_step(self, step):
        self.update_weights(step)
        self.update_positions()
        return self.best_value

    def update_weights(self, i):
        self.w = self.w * np.exp(-i / self.iterations)

    def update_positions(self):
        for j in range(self.num_agents):
            if np.random.rand() < self.w:
                self.population[j].position = self.population[j].position + np.random.rand() * (self.best_position - self.population[j].position)
            else:
                random_index = np.random.randint(0, self.num_agents - 1)
                random_pos = self.population[random_index].position
                self.population[j].position = self.population[j].position + self.z * np.random.rand() * (random_pos - self.population[j].position)

            self.population[j].position = self.population[j].position + self.vb * np.random.randn(self.dimensions)

            self.population[j].calculate_new_position()

            if self.population[j].value < self.best_value:
                self.best_value = self.population[j].value
                self.best_position = self.population[j].position
