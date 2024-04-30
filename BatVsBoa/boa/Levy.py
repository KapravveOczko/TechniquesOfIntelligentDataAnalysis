import numpy as np
import math


def levy_flight(alpha, size):
    sigma = (math.gamma(1 + alpha) * math.sin(np.pi * alpha / 2) / (math.gamma((1 + alpha) / 2) * alpha * 2
                                                                    ** ((alpha - 1) / 2))) ** (1 / alpha)
    u = np.random.normal(0, sigma, size)
    v = np.random.normal(0, 1, size)

    steps = u / (np.abs(v) ** (1 / alpha))

    return steps
