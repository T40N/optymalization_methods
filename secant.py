def secant(x0, x1, f, epsilon, max_iterations):
    for i in range(max_iterations):
        x2 = (f(x1) * x0 - f(x0) * x1) / (f(x1) - f(x0))
        y2 = f(x2)


        if abs(x2 - x1) <= epsilon:
            print(f"Liczba iteracji: {i}")
            print(f"Miejsce zerowe: {x2}")
            return x2

        x0 = x1
        x1 = x2

    print('Nie znaleziono miejsca zerowego')
    return False

n = 8

def f(x):
    return 2*n*x**5 + n**2*x**4 + 4*(1 - n)*x**3 + 2*n*(1 - n)*x**2 - 8*x - 4*n

secant(1, 2, f, 1e-4, 1000)