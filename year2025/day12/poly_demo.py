# Demo using polyomino package from https://github.com/jwg4/polyomino/
from polyomino.board import Rectangle
from polyomino.constant import MONOMINO
from polyomino.tileset import any_number_of

gifts = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 1), (2, 2)],
    [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)],
]

# 4x4 = 16 | [0, 0, 0, 0, 2, 0]
board = Rectangle(4, 4)
problem = board.tile_with_set(any_number_of([MONOMINO]).and_repeated_exactly(2, gifts[4]))
print("Solving Problem 1")
solution = problem.solve()
print(solution.display())

# 12x5 = 60 | [1, 0, 1, 0, 2, 2]
board = Rectangle(12, 5)
problem = board.tile_with_set(
    any_number_of([MONOMINO])
    .and_repeated_exactly(1, gifts[0])
    .and_repeated_exactly(1, gifts[2])
    .and_repeated_exactly(2, gifts[4])
    .and_repeated_exactly(2, gifts[5])
)
print("Solving Problem 2")
solution = problem.solve()
print(solution.display())

# 12x5 = 60 | [1, 0, 1, 0, 3, 2]
board = Rectangle(12, 5)
problem = board.tile_with_set(
    any_number_of([MONOMINO])
    .and_repeated_exactly(1, gifts[0])
    .and_repeated_exactly(1, gifts[2])
    .and_repeated_exactly(3, gifts[4])
    .and_repeated_exactly(2, gifts[5])
)
print("Solving Problem 3")
solution = problem.solve()
if solution:
    print(solution.display())
else:
    print("No solution")
