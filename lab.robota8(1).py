import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([0.4, 0.6, 0.9, 1.4])
y = np.array([2.45, 1.63, 0.95, 0.73])

# Розрахунок коефіцієнтів сплайну
cs = CubicSpline(x, y, bc_type='natural')

# Виведення коефіцієнтів сплайну
print("Коефіцієнти сплайну:")
print(cs.c)

# Розрахунок значень сплайну у вузлових точках
splined_values = cs(x)

# Виведення значень сплайну
print("Значення сплайну у вузлових точках:")
for i in range(len(x)):
    print(f"S({x[i]}) = {splined_values[i]}")
