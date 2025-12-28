from pprint import pprint

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

# Objective: minimize a + b + c + d + e + f
c = np.ones(6)

# Equality constraints
# Each row corresponds to one equation
A_eq = np.array(
    [
        # a  b  c  d  e  f
        [0, 0, 0, 0, 1, 1],  # e + f = 3
        [0, 1, 0, 0, 0, 1],  # b + f = 5
        [0, 0, 1, 1, 1, 0],  # c + d + e = 4
        [1, 1, 0, 1, 0, 0],  # a + b + d = 7
    ]
)

b_eq = np.array([3, 5, 4, 7])

constraints = LinearConstraint(A_eq, b_eq, b_eq)

# Non-negative bounds
bounds = Bounds(lb=[0] * 6, ub=[np.inf] * 6)

# All variables must be integers
integrality = np.ones(6, dtype=int)

result = milp(
    c=c,
    constraints=constraints,
    bounds=bounds,
    integrality=integrality,
)

pprint(result)
