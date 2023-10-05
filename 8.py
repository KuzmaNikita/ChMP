import numpy as np

# Матрица коэффициентов A
A = np.array([[3, -5, 3],
              [1, 2, 1],
              [2, 7, -1]])

# Вектор правых частей B
B = np.array([1, 4, 8])

# Вычисляем определитель матрицы A
detA = np.linalg.det(A)

if detA == 0:
    print("Метод Крамера не применим, так как определитель матрицы A равен 0.")
else:
    # Вычисляем обратную матрицу A_inv
    A_inv = np.linalg.inv(A)

    # Находим вектор решения X
    X = np.dot(A_inv, B)

    # Проверяем решение с использованием функции solve()
    X_check = np.linalg.solve(A, B)

    print("Решение методом Крамера (X):", X)
    print("Проверка с использованием solve() (X_check):", X_check)
