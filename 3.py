import numpy as np

# Определение матриц A и B
A = np.array([[3, 5],
              [6, -1]])

B = np.array([[2, 1],
              [-3, 2]])

# Вычисление произведения матриц A и B
result = np.dot(A, B)

print("Результат произведения матриц A и B:")
print(result)
