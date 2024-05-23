import numpy as np

    # - func: funkcja do minimalizacji
    # - x0: początkowy punkt startowy (numpy array)
    # - step_size: początkowy rozmiar kroku (default: 0.5)
    # - alpha: współczynnik przyspieszenia (default: 2)
    # - beta: współczynnik redukcji kroku (default: 0.5)
    # - tolerance: tolerancja dla kryterium stopu (default: 1e-5)
    # - max_iter: maksymalna liczba iteracji (default: 1000)


def hooke_jeeves(func, x0, step_size=0.5, alpha=2, beta=0.5, tolerance=1e-5, max_iter=1000):   
    iter = 0
    def exploratory_search(x, step_size):
        x_new = x.copy()
        for i in range(len(x)):
            x_temp = x_new.copy()
            x_temp[i] += step_size
            if func(x_temp) < func(x_new):
                x_new = x_temp
            else:
                x_temp[i] -= 2 * step_size
                if func(x_temp) < func(x_new):
                    x_new = x_temp
        return x_new

    x_best = np.array(x0)
    f_best = func(x_best)
    for iteration in range(max_iter):
        x_new = exploratory_search(x_best, step_size)
        if np.all(x_new == x_best):
            step_size *= beta
            if step_size < tolerance:
                break
        else:
            while True:
                x_temp = x_new + alpha * (x_new - x_best)
                x_best = x_new
                x_new = exploratory_search(x_temp, step_size)
                iter += 1
                if func(x_new) >= func(x_best):
                    break
        f_best = func(x_best)
    
    print(f"Liczba iteracji: {iter}")
    return x_best, f_best

n = 8

def rosenbrock2w(x):
    return (2 - x[0])**2 + (n + 2) * (x[1] - x[0]**2)**2

def rosenbrock3w(x):
    return (1 - x[0])**2 + n * (x[1] - x[0]**2)**2 + (1 - x[1])**2 + n * (x[2] - x[1]**2)**2

x0w2 = np.array([20, 20])
resultw2, valuew2 = hooke_jeeves(rosenbrock2w, x0w2)
print(f"Znaleziony punkt minimalny dla rosebrocka 2 wymiaru: {resultw2}")
print(f"Wartość funkcji w punkcie minimalnym dla rosebrocka 2 wymiaru: {valuew2:.20f}")

x0w3 = np.array([1.0, 2.0, 3.0])
resultw3, valuew3 = hooke_jeeves(rosenbrock3w, x0w3)
print(f"Znaleziony punkt minimalny dla rosebrocka 3 wymiaru: {resultw3}")
print(f"Wartość funkcji w punkcie minimalnym dla rosebrocka 3 wymiaru: {valuew3:.20f}")
