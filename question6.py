import numpy as np
from scipy.optimize import minimize

def obj_fun_1(x1, x2):
    return x1**2 + x1 + 2 * x2**2

def obj_fun_2(x1, x2):
    return np.sin(x1) + 0.5 * x2**2

def deriv_obj_fun_1(x1, x2):
    return (2 * x1 + 1, 4 * x2)

def deriv_obj_fun_2(x1, x2):
    return (np.cos(x1), x2)

# question1
def gradient_decs_1(n): # n is the iteration
    alpha = 0.01 # step size
    x1, x2 = 0, 0 # initial value
    f1 = obj_fun_1(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_1(x1, x2)
        x1 = x1 - alpha * deriv1
        x2 = x2 - alpha * deriv2
        f2 = obj_fun_1(x1, x2)
        if f1 - f2 < 1e-6: # stopping criterion
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

def gradient_decs_2(n):
    alpha = 0.01
    x1, x2 = 0, 0
    f1 = obj_fun_2(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_2(x1, x2)
        x1 = x1 - alpha * deriv1
        x2 = x2 - alpha * deriv2
        f2 = obj_fun_2(x1, x2)
        if f1 - f2 < 1e-6:
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

# question2
def gradient_decs_3(n):
    alpha_0 = 0.01 # initial step size
    lamda = 0.01 # decay rate
    x1, x2 = 0, 0
    f1 = obj_fun_1(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_1(x1, x2)
        alpha = alpha_0 / (1 + lamda * i)
        x1 = x1 - alpha * deriv1
        x2 = x2 - alpha * deriv2
        f2 = obj_fun_1(x1, x2)
        if f1 - f2 < 1e-6:
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

def gradient_decs_4(n):
    alpha_0 = 0.01
    lamda = 0.01
    x1, x2 = 0, 0
    f1 = obj_fun_2(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_2(x1, x2)
        alpha = alpha_0 / (1 + lamda * i)
        x1 = x1 - alpha * deriv1
        x2 = x2 - alpha * deriv2
        f2 = obj_fun_2(x1, x2)
        if f1 - f2 < 1e-6:
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

# question3
def gradient_decs_5(n):
    alpha = 0.01
    beta = 0.7 # shrinkage factor
    x1, x2 = 0, 0
    f1 = obj_fun_1(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_1(x1, x2)
        while True:
            x1 = x1 - alpha * deriv1
            x2 = x2 - alpha * deriv2
            f2 = obj_fun_1(x1, x2)
            # Armijo condition
            if f2 <= f1 - (alpha / 2) * (deriv1**2 + deriv2**2):
                break
            alpha *= beta
        if f1 - f2 < 1e-6:
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

def gradient_decs_6(n):
    alpha = 0.01
    beta = 0.7
    x1, x2 = 0, 0
    f1 = obj_fun_2(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_2(x1, x2)
        while True:
            x1 = x1 - alpha * deriv1
            x2 = x2 - alpha * deriv2
            f2 = obj_fun_2(x1, x2)
            if f2 <= f1 - (alpha / 2) * (deriv1**2 + deriv2**2):
                break
            alpha *= beta
        if f1 - f2 < 1e-6:
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

# question4
def gradient_decs_7(n):
    x1, x2 = 0, 0
    f1 = obj_fun_1(x1, x2)
    for i in range(n):
        deriv1, deriv2 = deriv_obj_fun_1(x1, x2)
        
        # line search
        def objective(alpha):
            x1_new = x1 - alpha * deriv1
            x2_new = x2 - alpha * deriv2
            return obj_fun_1(x1_new, x2_new)
        
        res = minimize(objective, x0 = 0, bounds = [(0, None)])
        alpha = res.x[0] # optimal step size
        
        x1 = x1 - alpha * deriv1
        x2 = x2 - alpha * deriv2
        f2 = obj_fun_1(x1, x2)
        if f1 - f2 < 1e-6:
            return float(x1), float(x2), float(f2)
        if f1 > f2:
            f1 = f2
    return float(x1), float(x2), float(f2)

if __name__ == "__main__":
    print(gradient_decs_1(1000))
    print(gradient_decs_2(1000))
    print(gradient_decs_3(1000))
    print(gradient_decs_4(1000))
    print(gradient_decs_5(1000))
    print(gradient_decs_6(1000))
    print(gradient_decs_7(1000))