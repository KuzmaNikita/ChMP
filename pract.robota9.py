import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

def f(x):
    return np.sin(4 * x)

x0 = np.pi / 6  

degree = 3  # Для аппроксимации первых трех производных

scale = 1.0  # Произвольное значение

taylor_poly = approximate_taylor_polynomial(f, x0, degree, scale)

x = np.linspace(0, 2 * np.pi, 100)

y = f(x)
taylor_y = taylor_poly(x)

# Построение графика функции и аппроксимации
plt.plot(x, y, label='f(x) = sin(4x)')
plt.plot(x, taylor_y, label=f'Taylor Polynomial (Degree {degree})')
plt.legend()
plt.title('Функция и аппроксимация полиномом Тейлора')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

