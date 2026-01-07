# nqueens.py
import random


class NQueens:
    def __init__(self, n: int):
        """
        Initialize N-Queens problem.

        :param n: Number of queens (size of board)
        """
        self.n = n

    # -----------------------------
    # State Representation
    # -----------------------------
    def random_state(self) -> list:
        """
        Generate a random state.
        Each column has exactly one queen placed at a random row.
        """
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    # -----------------------------
    # Cost Function (Heuristic)
    # -----------------------------
    def cost(self, state: list) -> int:
        """
        Calculate number of attacking queen pairs.
        Lower cost is better. Goal is cost == 0.
        """
        conflicts = 0

        for col1 in range(self.n):
            for col2 in range(col1 + 1, self.n):
                row1 = state[col1]
                row2 = state[col2]

                # Same row
                if row1 == row2:
                    conflicts += 1

                # Same diagonal
                if abs(row1 - row2) == abs(col1 - col2):
                    conflicts += 1

        return conflicts

    # -----------------------------
    # Generate Neighbors
    # -----------------------------
    def neighbors(self, state: list) -> list:
        """
        Generate all neighboring states by moving one queen
        in its column to a different row.
        """
        neighbors = []

        for col in range(self.n):
            current_row = state[col]

            for row in range(self.n):
                if row != current_row:
                    new_state = state.copy()
                    new_state[col] = row
                    neighbors.append(new_state)

        return neighbors
