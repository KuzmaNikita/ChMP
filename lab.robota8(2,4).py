import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Вхідні дані
x = np.array([0.4, 0.6, 0.9, 1.4])
y = np.array([2.45, 1.63, 0.95, 0.73])

# Розрахунок коефіцієнтів сплайну
cs = CubicSpline(x, y, bc_type='natural')

# Розрахунок значень сплайну у вузлових точках і перевірка їх співпадіння з вихідною функцією
for i in range(len(x)):
    interpolated_value = cs(x[i])
    original_value = y[i]
    print(f"x={x[i]}, S(x)={interpolated_value}, y={original_value}")

# Побудова графіка сплайну
xs = np.linspace(x.min(), x.max(), 100)
ys = cs(xs)

plt.figure()
plt.plot(x, y, 'o', label='Data points')
plt.plot(xs, ys, label='Cubic Spline')
plt.legend()
plt.xlabel('x')
plt.ylabel('Spline Value')
plt.title('Cubic Spline Interpolation')
plt.grid(True)
plt.show()
