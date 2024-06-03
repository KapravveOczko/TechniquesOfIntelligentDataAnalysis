
from .slime_mould_algorithm import SMA
from math import inf

class MS_SMA:
    def __init__(self, num_swarms, iterations, num_agents, dimensions, w, vb, z, func, bounds):
        self.num_swarms = num_swarms
        self.iterations = iterations
        self.num_agents = num_agents
        self.dimensions = dimensions
        self.w = w
        self.vb = vb
        self.z = z
        self.func = func
        self.bounds = bounds

        self.best_value = inf
        self.best_particle = None
        self.best_value_history = []
        self.swarms = [SMA(iterations, num_agents, dimensions, w, vb, z, func, bounds) for _ in range(num_swarms)]

    def run(self):
        for i in range(1, self.iterations):
            for swarm in self.swarms:
                swarm_best_value = swarm.run_by_step(i)

                if swarm_best_value < self.best_value:
                    self.best_value = swarm_best_value

            self.best_value_history.append(self.best_value)

        return self.best_value_history