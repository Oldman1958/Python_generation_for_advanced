"""
Напишите программу, которая рисует правильный треугольник.
"""

import turtle

# Настройка экрана и черепашки
screen = turtle.Screen()
screen.title("Правильный треугольник")
t = turtle.Turtle()
t.speed(3)          # Скорость рисования: 1–10, 0 — мгновенно
t.pensize(3)
t.color("darkblue")

# Параметры треугольника
side_length = 600   # Длина стороны

# Рисуем треугольник
t.penup()
# Центрируем треугольник на экране
t.goto(-side_length / 2, -side_length * 0.433)
t.pendown()

for _ in range(3):
    t.forward(side_length)
    t.left(120)     # Внешний угол для правильного треугольника — 120°

t.hideturtle()
screen.mainloop()
