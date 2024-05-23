import numpy as np

def gradient_descent(x0, y0, f, df_dx1, df_dx2, learning_rate, epsilon, max_iterations):
    for i in range(1, max_iterations + 1):
        gradient_x = df_dx1(x0, y0)
        gradient_y = df_dx2(x0, y0)

        next_x = x0 - learning_rate * gradient_x
        next_y = y0 - learning_rate * gradient_y

        gradient_norm = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
        position_difference_norm = np.sqrt((next_x - x0) ** 2 + (next_y - y0) ** 2)

        if gradient_norm <= epsilon or position_difference_norm <= epsilon:
            break

        if f(next_x, next_y) >= f(x0, y0):
            learning_rate *= 0.5
        else:
            x0 = next_x
            y0 = next_y

    print(f"Znalezione minimum: f({x0:.6f},{y0:.6f}) = {f(x0, y0):.6f}")
    print(f"Liczba iteracji: {i}")

n = 8

def df_dx1(x1, x2):
    return -2 * (n + 1 - x1) - 8 * x1 * (x2 - x1**2)

def df_dx2(x1, x2):
    return 4 * (x2 - x1**2)

def f(x1, x2):
    return (n + 1 - x1)**2 + 2 * (x2 - x1**2)**2

gradient_descent(0, 0, f, df_dx1, df_dx2, 0.1, 1e-6, 1000000)