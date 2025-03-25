import numpy as np
import cvxpy as cp

# Define parameters
T = 3
a = 1.5
alpha = 2

def compute_c_function(T):
    # Define variables
    u = cp.Variable(T-1)  # Control variable u_t
    x = cp.Variable(T)  # State variable x_t

    # Constraints
    # As we know the value of x, it can be seen as a constraint
    constraints = [x[0] == 1]  # Initial condition
    for t in range(1, T):
        constraints.append(x[t] == a * x[t-1] + u[t-1])  # Add new constraints to constraints

    # Define the cost function
    c = cp.sum_squares(x) + alpha*cp.sum_squares(u)

    return c, u, constraints  # Return function, control variable, and constraints

# Get function c(u), variable u, and constraints
c, u, constraints = compute_c_function(T)

# Solve the optimization problem
prob = cp.Problem(cp.Minimize(c), constraints)
prob.solve()

print("Optimal value of u:", u.value)
print("Minimum value of c:", c.value)