import entity


class Population:

    def __init__(self, a, b, num, size):
        self.population = self.generate_population(a, b, num, size)

    def generate_population(self, a, b, num, size):
        population = []

        for i in range(num):
            population.append(entity.Entity(a, b, size))

        return population

