""" 
Три квадрата с поворотом
"""

import turtle

# Настройка экрана и черепашки
screen = turtle.Screen()
screen.title("Три квадрата")
t = turtle.Turtle()
t.speed(3)          # Скорость рисования: 1–10, 0 — мгновенно
t.pensize(3)
t.color("darkred")

def sq(a):
    """
    Функция рисует квадрат со стороной а
    """
    for _ in range(4):
        t.forward(a)
        t.left(90)


dlina = 300

t.left(20)

for i in range(3):
    # Рисуем первый квадрат
    sq(dlina)
    # Поворачиваем тортиллу на 25 градусов влево
    t.left(25)
    # И далее в цикле рисуем еще два квадрата

# Сохраняем окно до закрытия
t.hideturtle()
screen.mainloop()
