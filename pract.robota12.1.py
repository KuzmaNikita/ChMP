import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def model(y, x):
    dydx = x + np.cos(y / np.exp(1))
    return dydx
y0 = 2.4
x_range = np.arange(1.4, 2.4 + 0.1, 0.1)
# Розв'язок диференціального рівняння за допомогою odeint
y_values = odeint(model, y0, x_range)
table_data = []
for i in range(len(x_range)):
    x_value = x_range[i]
    y_value = y_values[i][0]
    table_data.append((x_value, y_value))
    print(f"x = {x_value:.1f}, y = {y_value:.1f}")
plt.plot(x_range, y_values, label='odeint')
plt.scatter(*zip(*table_data), color='red', label='Checkpoints')
plt.title('Ейлер ')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()



