import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D plots
# Define the Rosenbrock function
def rosenbrock(x, y, a=1, b=100):
    return (a - x)**2 + b * (y - x**2)**2

# Define y = x^2 function
def parabola(x):
    return x**2

# Create grid
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Compute Rosenbrock function values
Z_rosenbrock = rosenbrock(X, Y)  # non-convex nor concave

# Compute y = x^2 function values
Z_parabola = parabola(X) #convex
 
# Create 3D plot
fig = plt.figure(figsize=(10, 4))

# Plot Rosenbrock function
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z_rosenbrock, cmap='inferno')
ax1.set_title('Rosenbrock Function')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Plot y = x^2 function
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z_parabola, cmap='viridis')
ax2.set_title('$y = x^2$ Function')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# Show plot
plt.tight_layout()
plt.show()

# 2D plots
# Define x values
x = np.linspace(-10, 10, 400)

# Define y expressions
y1 = 10 * x ** 2  # convex
y2 = x ** 3 + x ** 2  # non-convex function

# Create 2D plot
plt.figure(figsize=(8, 4))
plt.plot(x, y1, label=r'$y = 10x^2 \quad convex$', linestyle='-', color='b')
plt.plot(x, y2, label=r'$y = x^3 + x^2 \quad not\ convex$', linestyle='--', color='r')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = 10x^2$ and $y = x^3 + x^2$')

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend()

# Show plot
plt.show()
