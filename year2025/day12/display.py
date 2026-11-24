import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Example grid (0 = ".", A=1, B=2, C=3, ...)
grid = np.array(
    [
        [0, 0, 0, 0, 1, 1, 1, 6, 6, 5, 5, 5],
        [0, 2, 2, 2, 1, 1, 6, 6, 6, 5, 5, 5],
        [4, 4, 4, 2, 1, 1, 6, 6, 3, 5, 3, 5],
        [4, 2, 2, 2, 0, 0, 0, 0, 3, 3, 3, 0],
        [4, 4, 4, 0, 0, 0, 0, 0, 3, 0, 3, 0],
    ]
)

# Index 0 = empty
letters = ["", "A", "B", "C", "D", "E", "F"]

# Colors (first is background / dots)
colors = [
    "#000000",  # empty
    "#ff9999",  # A
    "#99ccff",  # B
    "#99ff99",  # C
    "#ffd966",  # D
    "#c299ff",  # E
    "#ffcc99",  # F
]

cmap = ListedColormap(colors)

plt.figure(figsize=(6, 4))
plt.imshow(grid, cmap=cmap)
plt.axis("off")

# Draw letters (skip zeros)
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        value = grid[y, x]
        if value != 0:
            plt.text(x, y, letters[value], ha="center", va="center", color="black", fontsize=12, fontweight="bold")

plt.tight_layout()
plt.show()
