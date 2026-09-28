""" 
Нарисуйте домик по образцу (см. задание на сайте)
"""
import turtle
import math

screen = turtle.Screen()
screen.title("Домик")
t = turtle.Turtle()
t.speed(3)
t.pensize(3)
t.color("black")

# Размеры домика
wall_width = 200
wall_height = 150

# Рисуем стены (с заливкой)
t.penup()
t.goto(-wall_width / 2, -wall_height)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
for _ in range(2):
    t.forward(wall_width)
    t.left(90)
    t.forward(wall_height)
    t.left(90)
t.end_fill()

# Ширина крыши на 20% шире стен
roof_width = wall_width * 1.2
half_roof = roof_width / 2

# Основание крыши: левый край на half_roof левее центра, правый — на half_roof правее
roof_left_x = -half_roof
roof_right_x = half_roof
# это верхняя линия стен (так как стены идут от -wall_height до 0)
y_top_walls = 0

# Высота равнобедренного треугольника по теореме Пифагора:
# половина основания = roof_width/2, угол при основании можно выбрать,
# но проще взять высоту так, чтобы крыша смотрелась гармонично.
# Сделаем высоту крыши = половина ширины крыши — получится приятный наклон.
roof_height = roof_width / 2

# Координаты вершины крыши
peak_x = 0
peak_y = y_top_walls + roof_height

# Рисуем крышу
t.penup()
# левый верхний угол стен — старт основания крыши
t.goto(roof_left_x, y_top_walls)
t.pendown()

t.fillcolor("brown")
t.begin_fill()

# Левая сторона: от левого края основания к вершине
t.setheading(t.towards(peak_x, peak_y))
t.goto(peak_x, peak_y)

# Правая сторона: от вершины к правому краю основания
t.setheading(t.towards(roof_right_x, y_top_walls))
t.goto(roof_right_x, y_top_walls)

# Замыкаем основание (обратно к старту)
t.goto(roof_left_x, y_top_walls)

t.end_fill()

t.hideturtle()
screen.mainloop()
