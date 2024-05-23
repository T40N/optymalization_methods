import numpy as np

# - function: The function to be minimized.
# - x0: The initial point for the optimization.
# - delta: The initial step size for the search. Default is 1e-2.
# - beta: The reduction factor for the step size. Default is 0.5.
# - epsilon: The tolerance for stopping the optimization. Default is 1e-8.

def minimize(function, x0, delta=1e-2, beta=0.5, epsilon=1e-8):
    xb = np.copy(x0)
    f0 = function(xb)

    iter = 0
    while True:
        for i in range(len(x0)):
            z = np.copy(x0)
            z[i] += delta 

            f = function(z)

            if f < f0:  
                f0 = f
                xb = np.copy(z)
            else:
                z = np.copy(x0)
                z[i] -= 2 * delta
                f = function(z)

                if f < f0: 
                    f0 = f
                    xb = np.copy(z)

        if function(xb) < function(x0):
            x0 = np.copy(xb)
        else:
            if delta < epsilon:
                print(f"Points: {x0}")
                print(f"Value: {f0:.15f}")
                print(f"Iterations: {iter}")
                break
            else:
                delta *= beta

        for i in range(len(x0)):
            x0[i] = 2 * xb[i] - x0[i]
        iter += 1

n = 8

def f2d(x):
    return (2 - x[0])**2 + (n + 2) * (x[1] - x[0]**2)**2

def f3d(x):
    return (1 - x[0])**2 + n * (x[1] - x[0]**2)**2 + (1 - x[1])**2 + n * (x[2] - x[1]**2)**2

print("--------------------")
print("Funkcja rossenbrocka 2D")
x0 = np.array([1.0, 2.0])
minimize(f2d, x0)
print("--------------------")
print("Funkcja rossenbrocka 3D")
x0 = np.array([1.0, 2.0, 20.0])
minimize(f3d, x0)
