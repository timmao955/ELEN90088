import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

l = cp.Variable(pos=True)
w = cp.Variable(pos=True)

constraints = [l + 2*w <= 60]

objective = cp.Maximize(l * w)
problem = cp.Problem(objective, constraints)
problem.solve(gp=True)

print("Length:", l.value)
print("Width:", w.value)
print("Area:", l.value * w.value)

w = np.linspace(0.1, 30, 100)
l = 60 - 2 * w
A = l * w
plt.plot(w, A, label='Area = w * (60 - 2w)')
plt.axvline(15, color='red', linestyle='--', label='Optimal width = 15m')
plt.axhline(450, color='green', linestyle='--', label='Max area = 450 m²')
plt.xlabel('Width (m)')
plt.ylabel('Area (m^2)')
plt.grid(True)
plt.show()
