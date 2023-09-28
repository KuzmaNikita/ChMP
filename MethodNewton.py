def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 5

def f_prime(x):
    return 4*x**3 + 6*x**2 + 4*x + 6

def newton_method(initial_guess, tolerance):
    x0 = initial_guess
    while True:
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tolerance:
            return x1
        x0 = x1

initial_guess = 1.0  # Початкове наближення
tolerance = 0.0001   # Точність

result = newton_method(initial_guess, tolerance)
print("Розв'язок:", result)
