import numpy as np
import random

# Встановлення розмірності матриці
N = 5  # Кількість рядків
M = 4  # Кількість стовпців

# Генерування прямокутної матриці з випадковими значеннями
matrix = np.random.randint(-10, 10, size=(N, M))

# Виведення згенерованої матриці
print("Згенерована матриця:")
print(matrix)

# Знайдемо кількість негативних елементів в кожному рядку та в кожному стовпці
negatives_in_rows = [np.sum(row < 0) for row in matrix]
negatives_in_columns = [np.sum(matrix[:, col] < 0) for col in range(M)]

# Виведення результатів
print("Кількість негативних елементів в кожному рядку:", negatives_in_rows)
print("Кількість негативних елементів в кожному стовпці:", negatives_in_columns)
