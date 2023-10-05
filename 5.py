import numpy as np

# Определение матрицы
matrix = np.array([[1, 2, 3, 4],
                  [-2, 1, -4, 3],
                  [3, -4, -1, 2],
                  [4, 3, -2, -1])

# Вычисление определителя
determinant = np.linalg.det(matrix)

print("Определитель матрицы:")
print(determinant)
