import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

def obj_fun():
    # matrix G
    np.random.seed(42)
    G = np.random.uniform(0.1, 0.9, (N, N))
    np.fill_diagonal(G, 1.0)

    P = cp.Variable(N, pos=True)
    objective = cp.Minimize(cp.sum(P))

    # SINR is not a constraint when S_min = 0
    constraints = [P >= P_min, P <= P_max]

    prob = cp.Problem(objective, constraints)
    prob.solve(gp=True)

    SINR = [G[i,i] * P.value[i] / (sigma + sum(G[i,k] * P.value[k] for k in range(N) if k != i)) for i in range(N)]

    print("Power levels: ", P.value)
    print("SINR: ", SINR)

    return P.value, SINR

def obj_fun_large_sm(N, P_min, P_max, sigma, S_min):
    np.random.seed(42)

    G = np.random.uniform(0.1, 0.9, (N, N))
    np.fill_diagonal(G, 1.0)

    P = cp.Variable(N, pos=True)
    objective = cp.Minimize(cp.sum(P))
    constraints = [P_min / P <= 1.0, P / P_max <= 1.0]

    for i in range(N):
        tmp = cp.sum([G[i, k] * P[k] for k in range(N) if k != i])
        sinr_inv_expr = (sigma + tmp) / (G[i, i] * P[i])
        constraints.append(sinr_inv_expr <= 1.0 / S_min)

    prob = cp.Problem(objective, constraints)
    prob.solve(gp = True)

    print(f"S_min = {S_min}: Status = {prob.status}, Power levels = {P.value}")

def plot_graph(P_opt, SINR):
    plt.figure()
    plt.bar(range(N), P_opt)
    plt.xlabel('Transmitter Index (N)')
    plt.ylabel('Power levels')
    plt.show()

    plt.figure()
    plt.bar(range(N), SINR)
    plt.xlabel('Receiver Index (N)')
    plt.ylabel('SINR')
    plt.show()

if __name__ == "__main__":
    N = 10
    P_min = 0.1
    P_max = 5
    sigma = 0.2
    # S_min = 0
    S_min = [0.1, 0.2, 0.5, 1.0, 2.0, 10.0]

    # P_opt, SINR = obj_fun()
    # plot_graph(P_opt, SINR)
    for sm in S_min:
        obj_fun_large_sm(N, P_min, P_max, sigma, sm)

    