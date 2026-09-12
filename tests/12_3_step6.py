""" 
Напишите программу, которая при помощи метода Монте-Карло вычисляет 
и выводит площадь фигуры, задаваемой с помощью системы неравенств:



  
−2≤x≤2
−2≤y≤2
x ^ 3  + y ^ 4  +2≥0
3x+y ^ 2  ≤2
​
"""

import random


def is_in_figure(x, y):
    return (
        -2 <= x <= 2
        and -2 <= y <= 2
        and x**3 + y**4 + 2 >= 0
        and 3*x + y**2 <= 2
    )


n = 10**6  # количество испытаний

count = 0
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if is_in_figure(x, y):
        count += 1

# Площадь прямоугольника [-2, 2] × [-2, 2] = 4 × 4 = 16
area = count / n * 16
print(area)
