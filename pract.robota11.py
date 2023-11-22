from scipy import integrate
import math

# Задані функції для інтегрування
def func1(x):
    return 1 / ((3*x - 1)**0.5)

def func2(x):
    return math.log(x**2 + 1) / x

def func3(x):
    return 1 / (0.2*x**2 + 1)**0.5

# Метод прямокутників
def rectangle_method(func, a, b, n):
    h = (b - a) / n
    integral_sum = sum(func(a + i * h) for i in range(n))
    result = h * integral_sum
    return result

# Метод Сімпсона
def simpson_method(func, a, b, n):
    integral_result = integrate.simps([func(a + i * (b - a) / n) for i in range(n+1)], dx=(b - a) / n)
    return integral_result

# Метод трапецій
def trapezoid_method(func, a, b, n):
    h = (b - a) / n
    nodes = [func(a + i * h) for i in range(n + 1)]
    integral_result = h * (sum(nodes) - 0.5 * (nodes[0] + nodes[n]))
    return integral_result

# Точність до 0.0001
precision = 0.0001

# Параметри для обчислень
integrals = [(func1, 1.4, 2.1), (func2, 0.8, 1.6), (func3, 1.3, 2.5)]
methods = [rectangle_method, simpson_method, trapezoid_method]
p_values = [10, 8, 20]

for i, (func, a, b) in enumerate(integrals):
    print(f"Інтеграл {i + 1} (від {a} до {b}):")
    method = methods[i]
    n = p_values[i]
    result = method(func, a, b, n)
    print(f"Метод {i + 1}: {result:.4f}\n")
