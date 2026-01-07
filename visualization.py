# visualization.py

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def draw_chessboard(state, queen_image_path):
    """
    Draw an N-Queens solution on a clean black & white chessboard.
    """
    n = len(state)

    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw chessboard squares
    for row in range(n):
        for col in range(n):
            color = "white" if (row + col) % 2 == 0 else "red"
            ax.add_patch(
                plt.Rectangle(
                    (col, n - row - 1), 1, 1, color=color
                )
            )

    # Load and resize queen image
    queen_img = Image.open(queen_image_path).convert("RGBA")
    queen_img = queen_img.resize((80, 80))  # 👈 اندازه ثابت و منطقی

    # Draw queens
    for col, row in enumerate(state):
        ax.imshow(
            queen_img,
            extent=(
                col + 0.1,
                col + 0.9,
                n - row - 0.9,
                n - row - 0.1,
            ),
            zorder=10,
        )

    # Formatting
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    ax.set_title(f"{n}-Queens Solution", fontsize=14)

    plt.tight_layout()
    plt.show()
