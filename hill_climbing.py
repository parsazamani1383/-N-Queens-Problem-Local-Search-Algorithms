# hill_climbing.py

from nqueens import NQueens


def hill_climbing(problem: NQueens, initial_state: list):
    """
    Perform Hill Climbing algorithm for N-Queens.

    :param problem: NQueens problem instance
    :param initial_state: Starting state
    :return: final_state, final_cost, steps
    """
    current_state = initial_state
    current_cost = problem.cost(current_state)
    steps = 0

    while True:
        neighbors = problem.neighbors(current_state)

        # Find best neighbor
        best_neighbor = current_state
        best_cost = current_cost

        for neighbor in neighbors:
            neighbor_cost = problem.cost(neighbor)

            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost

        # If no improvement, stop
        if best_cost >= current_cost:
            break

        current_state = best_neighbor
        current_cost = best_cost
        steps += 1

    return current_state, current_cost, steps
