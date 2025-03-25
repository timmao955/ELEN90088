import cvxpy as cp
import numpy as np

# Define the variables
u_1 = cp.Variable()
u_2 = cp.Variable()

# Define the objective function
c = 1 + (1.5 + u_1)**2 + (2.25 + 1.5*u_1 + u_2)**2 + 2*u_1**2 + 2*u_2**2

# Formulate the problem
objective = cp.Minimize(c)
problem = cp.Problem(objective)

# Solve the problem
problem.solve()

# Print the results
print("Optimal value of u_1:", u_1.value)
print("Optimal value of u_2:", u_2.value)
print("Minimum value of c:", c.value)