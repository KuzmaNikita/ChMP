import numpy as np
from scipy.interpolate import CubicSpline

# Вхідні дані 
x_user = np.array([0.5, 1.0, 1.2])  
x_data = np.array([0.4, 0.6, 0.9, 1.4])
y_data = np.array([2.45, 1.63, 0.95, 0.73])

# Розрахунок коефіцієнтів сплайну
cs = CubicSpline(x_data, y_data, bc_type='natural')

# Розрахунок значень сплайну в користувацьких точках
splined_values_user = cs(x_user)


for i in range(len(x_user)):
    print(f"x_user={x_user[i]}, S(x_user)={splined_values_user[i]}")
