# random_restart.py

from nqueens import NQueens
from hill_climbing import hill_climbing


def random_restart_hill_climbing(problem: NQueens, max_restarts: int):
    """
    Perform Hill Climbing with Random Restart.

    :param problem: NQueens problem instance
    :param max_restarts: Maximum number of restarts
    :return: best_state, best_cost, total_restarts, total_steps
    """
    best_state = None
    best_cost = float("inf")
    total_steps = 0

    for restart in range(1, max_restarts + 1):
        initial_state = problem.random_state()
        final_state, final_cost, steps = hill_climbing(problem, initial_state)

        total_steps += steps

        if final_cost < best_cost:
            best_state = final_state
            best_cost = final_cost

        # Perfect solution found
        if best_cost == 0:
            break

    return best_state, best_cost, restart, total_steps
