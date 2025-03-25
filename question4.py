import numpy as np
import matplotlib.pyplot as plt

def plot_graph(N):
    p = np.linspace(0, 1, 1000)
    S = N * p * (1 - p)**(N - 1)
    plt.plot(p, S, label=f'N = {N}')
    plt.xlabel('p', fontsize=14)
    plt.ylabel('S', fontsize=14)
    plt.grid(True)
    plt.show()

def maximum_s(N):
    p = 1 / N
    S_max = N * p * (1 - p) ** (N - 1)
    print(f"The maximum value of S ≈ {S_max:.6f}")

if __name__ == "__main__":
    plot_graph(10)
    maximum_s(10000)
