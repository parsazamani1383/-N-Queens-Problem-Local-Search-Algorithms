# simulated_annealing.py

import math
import random
from nqueens import NQueens


def simulated_annealing(
    problem: NQueens,
    initial_state: list,
    initial_temperature: float,
    cooling_rate: float,
    max_steps: int
):
    """
    Perform Simulated Annealing for N-Queens.

    :param problem: NQueens problem instance
    :param initial_state: Starting state
    :param initial_temperature: Initial temperature
    :param cooling_rate: Temperature reduction factor (0 < cooling_rate < 1)
    :param max_steps: Maximum number of steps
    :return: final_state, final_cost, steps
    """
    current_state = initial_state
    current_cost = problem.cost(current_state)
    temperature = initial_temperature
    steps = 0

    while temperature > 0.001 and steps < max_steps and current_cost > 0:
        steps += 1

        # Pick a random neighbor
        neighbors = problem.neighbors(current_state)
        next_state = random.choice(neighbors)
        next_cost = problem.cost(next_state)

        delta = next_cost - current_cost

        # Accept better state
        if delta < 0:
            current_state = next_state
            current_cost = next_cost
        else:
            # Accept worse state with some probability
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current_state = next_state
                current_cost = next_cost

        # Cool down
        temperature *= cooling_rate

    return current_state, current_cost, steps
