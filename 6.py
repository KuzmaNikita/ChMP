import numpy as np

# Определение матрицы
matrix = np.array([[1, 2, 2],
                  [2, 1, -2],
                  [2, -2, 1]])

# Попробуем найти обратную матрицу
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Обратная матрица:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Обратная матрица не существует, так как определитель равен 0.")
