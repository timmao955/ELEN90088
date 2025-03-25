import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Rosenbrock function, a common test function for optimization algorithms
def rosenbrock(x, y, a=1, b=100):
    return (a - x) ** 2 + b * (y - x ** 2) ** 2

# Define a simple power function
def power(x, m=2):
    """
    Computes x raised to the power of m.

    :param x: Input value
    :param m: Exponent (default = 2)
    :return: x^m
    """
    return x ** m

# Generate X, Y values over a grid
x = np.linspace(-2, 2, 400)  # X range from -2 to 2
y = np.linspace(0, 2, 400)  # Y range from -2 to 2
X, Y = np.meshgrid(x, y)  # Create meshgrid for surface plot

# Compute function values
Z = rosenbrock(X, Y)  # Rosenbrock function values
Z1 = power(X, Y)  # Power function values

# Create two figures for separate plots
fig1 = plt.figure(figsize=(12, 5))  # Figure for 3D surface plot
fig2 = plt.figure(figsize=(12, 5))  # Figure for 2D function plot

# --- 3D Surface Plot of Rosenbrock Function ---
ax1 = fig1.add_subplot(111, projection='3d')  # 3D axis
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)  # Plot surface with color map

# Label axes
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('f(X, Y)')
ax1.set_title('Rosenbrock Function (3D)')

# --- 2D Plot of y = x^2 ---
x = np.linspace(-10, 10, 400)  # X values from -10 to 10
y = x ** 2  # Compute Y values for y = x^2

plt.plot(x, y, label='y = x^2', color='b')  # Plot function

# Add labels and title
plt.title('Graph of y = x^2')
plt.xlabel('x')
plt.ylabel('y')

# Enable grid and legend
plt.grid(True)
plt.legend()

# Show the 2D plot
plt.show()

# Show the 3D surface plot
plt.show()