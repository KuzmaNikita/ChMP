import numpy as np
import matplotlib.pyplot as plt
x0 = 0.5
y0 = 0.6
h = 0.1
x_range = np.arange(0.5, 1.5 + h, h)
def f(x, y):
    return x + np.sin(y / (7**0.5))
def euler_cauchy_method(x0, y0, h, x_range):
    x_values = [x0]
    y_values = [y0]
    for x in x_range[:-1]:
        y0 = y0 + h * f(x, y0)
        x_values.append(x + h)
        y0 = y0 + h * f(x + h, y0)
        y_values.append(y0)
    return x_values, y_values
x_values, y_values = euler_cauchy_method(x0, y0, h, x_range)
x_values_rounded = [round(value, 1) for value in x_values]
y_values_rounded = [round(value, 1) for value in y_values]
for i in range(len(x_values)):
    print(f"x = {x_values_rounded[i]}, y = {y_values_rounded[i]}")
plt.plot(x_values, y_values, label='Euler-Cauchy Method', marker='o')
plt.title('Ейлер-Коші Метод ')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()






