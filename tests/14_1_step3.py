"""
Напишите программу, которая рисует правильный треугольник.
"""

import  turtle
turtle.showturtle()
def triangle(side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)
triangle(400)