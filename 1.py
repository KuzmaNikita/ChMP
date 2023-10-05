import numpy as np

# Определение матриц A и B
A = np.array([[2, 3, 1],
              [-1, 1, 0],
              [1, 2, -1]])

B = np.array([[1, 2, 1],
              [0, 1, 2],
              [3, 1, 1]])

# Вычисление C = AB - BA
C = np.dot(A, B) - np.dot(B, A)

print("Матрица C:")
print(C)
