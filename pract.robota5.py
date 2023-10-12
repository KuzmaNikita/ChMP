import math
# Початкові наближення
x = 1.2
y = 1.6

# Параметр для зупинки ітерації
epsilon = 0.001

# Максимальна кількість ітерацій
max_iterations = 1000

for i in range(max_iterations):
    # Оновлюємо значення x та y за допомогою функцій системи рівнянь
    new_x = math.sin(y - 1) + 1.3
    new_y = math.sin(x - 0.8) - 1

    # Обчислюємо похибку
    error_x = abs(new_x - x)
    error_y = abs(new_y - y)

    # Оновлюємо значення x та y
    x = new_x
    y = new_y

    # Перевіряємо умову завершення ітерації
    if error_x < epsilon and error_y < epsilon:
        break
print(f"Результат: x = {x:.3f}, y = {y:.3f}")
