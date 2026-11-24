from pprint import pprint

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

b_eq = np.array([7, 5, 12, 7, 2])
size = len(b_eq)

# Objective: minimize a + b + c + d + e + f
c = np.ones(size)

# Equality constraints
# Each row corresponds to one equation
# A_eq = np.array(
#     [
#         # a  b  c  d  e  f
#         [0, 0, 0, 0, 0, 0, 0],  #
#         [0, 0, 0, 0, 0, 0, 0],  #
#         [0, 0, 0, 0, 0, 0, 0],  #
#         [0, 0, 0, 0, 0, 0, 0],  #
#         [0, 0, 0, 0, 0, 0, 0],  #
#     ]
# )
A_eq = np.array(
    [
        [1, 0, 1, 1, 0],  #
        [0, 0, 0, 1, 1],  #
        [1, 1, 0, 1, 1],  #
        [1, 1, 0, 0, 1],  #
        [1, 0, 1, 0, 1],  #
    ]
)

constraints = LinearConstraint(A_eq, b_eq, b_eq)

# Non-negative bounds
bounds = Bounds(lb=[0] * size, ub=[np.inf] * size)

# All variables must be integers
integrality = np.ones(size, dtype=int)

result = milp(
    c=c,
    constraints=constraints,
    bounds=bounds,
    integrality=integrality,
)

pprint(result)
