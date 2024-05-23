def bisection(a, b, f, epsilon, max_iterations):
    for i in range(max_iterations):
        x = (a + b) / 2
        y = f(x)

        print(f"Iter: {i + 1}, x: {x}, f: {y}")

        if abs(y) <= epsilon:
            print
            print(f"Miejsce zerowe: {x}")
            return x

        if f(a) * y < 0:
            b = x
        else:
            a = x

    print('Nie znaleziono miejsca zerowego')
    return False