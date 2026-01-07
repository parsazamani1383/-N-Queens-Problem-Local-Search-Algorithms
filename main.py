# main.py

from nqueens import NQueens
from hill_climbing import hill_climbing
from random_restart import random_restart_hill_climbing
from simulated_annealing import simulated_annealing
from visualization import draw_chessboard


def run_hill_climbing(problem):
    print("\nRunning Hill Climbing...")
    initial_state = problem.random_state()
    state, cost, steps = hill_climbing(problem, initial_state)

    print(f"Final Cost: {cost}")
    print(f"Steps Taken: {steps}")
    return state, cost


def run_random_restart(problem):
    print("\nRunning Hill Climbing with Random Restart...")
    state, cost, restarts, steps = random_restart_hill_climbing(
        problem,
        max_restarts=500
    )

    print(f"Final Cost: {cost}")
    print(f"Restarts: {restarts}")
    print(f"Total Steps: {steps}")
    return state, cost


def run_simulated_annealing(problem):
    print("\nRunning Simulated Annealing...")
    initial_state = problem.random_state()

    state, cost, steps = simulated_annealing(
        problem,
        initial_state,
        initial_temperature=1000,
        cooling_rate=0.995,
        max_steps=10000
    )

    print(f"Final Cost: {cost}")
    print(f"Steps Taken: {steps}")
    return state, cost


def main():
    N = 8
    queen_image_path = "assets/queen.png"

    problem = NQueens(N)

    print("N-Queens Problem Solver")
    print("1 - Hill Climbing")
    print("2 - Hill Climbing with Random Restart")
    print("3 - Simulated Annealing")

    choice = input("Select algorithm (1/2/3): ")

    if choice == "1":
        state, cost = run_hill_climbing(problem)
    elif choice == "2":
        state, cost = run_random_restart(problem)
    elif choice == "3":
        state, cost = run_simulated_annealing(problem)
    else:
        print("Invalid choice!")
        return

    if cost == 0:
        print("Solution found!")
    else:
        print("Local optimum reached (not a perfect solution).")

    draw_chessboard(state, queen_image_path)


if __name__ == "__main__":
    main()
