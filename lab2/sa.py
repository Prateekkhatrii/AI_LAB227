
import random
import math

def objective(x):
    return x * x

def simulated_annealing():
    current = random.uniform(-10, 10)
    best = current
    temperature = 100

    while temperature > 0.01:
        next_x = current + random.uniform(-1, 1)
        next_x = max(-10, min(10, next_x))

        delta = objective(next_x) - objective(current)

        if delta < 0:
            current = next_x
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current = next_x

        if objective(current) < objective(best):
            best = current

        temperature *= 0.95

    print("Best solution:", best)
    print("Minimum value:", objective(best))

simulated_annealing()
