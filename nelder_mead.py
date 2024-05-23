import numpy as np

ALPHA = 1.0  # reflection coefficient
BETA = 0.5  # contraction coefficient
GAMMA = 2.0  # expansion coefficient
DELTA = 0.5  # reduction coefficient
EPSILON = 0.0000001  # tolerance

def function2D(x):
    n = 8
    return (3 - x[0])**2 + (n + 2) * (x[1] - x[0]**2)**2

def function3D(x):
    n = 8
    return (1 - x[0])**2 + n * (x[1] - x[0]**2)**2 + (1 - x[1])**2 + n * (x[2] - x[1]**2)**2

def sort_points(values, points):
    indices = np.argsort(values)
    sorted_points = points[indices]
    return sorted_points

def build_simplex(dimensions):
    first_point = np.zeros(dimensions)
    for i in range(dimensions):
        first_point[i] = float(input("Enter number: " + str(i) + ": "))

    simplex = np.zeros((dimensions + 1, dimensions))
    for i in range(dimensions + 1):
        simplex[i] = first_point
        if i > 0:
            simplex[i][i - 1] += 1.0

    return simplex


def minimize(function, dimensions):
    simplex = build_simplex(dimensions)
    print("Simplex: ", simplex)
    f_values = np.zeros(dimensions + 1)

    while True:
        for i in range(dimensions + 1):
            f_values[i] = function(simplex[i])

        simplex = sort_points(f_values, simplex)

        centroid = np.mean(simplex[:-1], axis=0)

        reflected = (1 + ALPHA) * centroid - ALPHA * simplex[-1]
        f_reflected = function(reflected)

        if f_reflected < f_values[0]:
            expanded = GAMMA * reflected + (1 - GAMMA) * centroid
            f_expanded = function(expanded)

            if f_expanded < f_values[0]:
                simplex[-1] = expanded
                f_values[-1] = f_expanded
            else:
                simplex[-1] = reflected
                f_values[-1] = f_reflected
        elif f_values[0] <= f_reflected <= f_values[-2]:
            simplex[-1] = reflected
            f_values[-1] = f_reflected
        else:
            if f_values[-2] < f_reflected < f_values[-1]:
                simplex[-1] = reflected
                f_values[-1] = f_reflected

            contraction = BETA * simplex[-1] + (1 - BETA) * centroid
            f_contraction = function(contraction)

            if f_contraction < f_values[-1]:
                simplex[-1] = contraction
                f_values[-1] = f_contraction
            else:
                for i in range(dimensions + 1):
                    simplex[i] = simplex[i] + simplex[0] * DELTA
                    f_values[i] = function(simplex[i])

        f_centroid = function(centroid)
        value = np.sqrt(np.sum((f_values - f_centroid)**2) / (dimensions + 1))

        if value <= EPSILON:
            break
    
    print("Minimum point: ", simplex[0])
    print(f"Minimum value: {f_values[0]:.12f}")


if __name__ == "__main__":
    function = None
    while True:
        dimensions = int(input("Number of dimensions: "))
        if dimensions == 2:
            function = function2D
            break
        elif dimensions == 3:
            function = function3D
            break
        else:
            print("Enter 2 or 3!")

    minimize(function, dimensions)