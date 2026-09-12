""" 
Напишите программу, которая при помощи метода Монте-Карло 
определяет приближённое значение числа π и выводит его.
"""

import random


def estimate_pi(num_points: int) -> float:
    inside_circle = 0

    for _ in range(num_points):
        # Генерируем случайную точку в квадрате [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Проверяем, лежит ли точка внутри единичного круга
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Площадь круга / площадь квадрата = π / 4
    # Значит, π ≈ 4 * (точки внутри круга / всего точек)
    return 4 * inside_circle / num_points


n = 1_000_000  # количество случайных точек
pi_approx = estimate_pi(n)
print(f"Приближённое значение π: {pi_approx}")
