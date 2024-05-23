def newton(x0, f, df, epsilon, max_iterations):
    iter = 0
    for i in range(max_iterations):
        y = f(x0)
        dfx = df(x0)
        iter += 1

        if abs(dfx) < 0:
            print("Nie znaleziono");
            break


        x1 = x0 - (y / dfx)

        if abs(x1 - x0) <= epsilon:
            print(f"Liczba iteracji: {iter}")
            print(f"Miejsce zerowe: {x1}")
            return x1

        x0 = x1

    print('Nie znaleziono miejsca zerowego')
    return False

n = 8

def f(x):
    return 2*n*x**5 + n**2*x**4 + 4*(1 - n)*x**3 + 2*n*(1 - n)*x**2 - 8*x - 4*n

def df(x):
    return 10*n*x**4 + 4*n**2*x**3 + 12*(1 - n)*x**2 + 4*n*(1 - n)*x - 8

newton(1, f, df, 1e-4, 1000)