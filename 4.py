import numpy as np

# Определение матрицы
matrix = np.array([[2, 3, 4],
                  [1, 0, 6],
                  [7, 8, 9]])

# Вычисление определителя
determinant = np.linalg.det(matrix)

print("Определитель матрицы:")
print(determinant)
