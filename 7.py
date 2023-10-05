import numpy as np

# Определение матрицы
matrix = np.array([[1, 2, 3, 4],
                  [3, -1, 2, 5],
                  [1, 2, 3, 4],
                  [1, 3, 4, 5]])

# Вычисление ранга матрицы
rank = np.linalg.matrix_rank(matrix)

print("Ранг матрицы:", rank)
