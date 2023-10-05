import numpy as np

# Определение матрицы
matrix = np.array([[-1, 2],
                   [0, 1]])

# Возведение матрицы в степень 2
result = np.linalg.matrix_power(matrix, 2)

print("Результат возведения матрицы в степень 2:")
print(result)
