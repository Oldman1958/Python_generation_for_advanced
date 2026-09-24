"""
Напишите программу, которая рисует прямоугольник.

Примечание 1. 
Программу нужно оформить в виде функции rectangle(width, height), 
где width, height – ширина и высота прямоугольника.

Примечание 2. 
Для написания и запуска кода используйте IDE на своем компьютере или онлайн-визуализатор ниже.
"""


def rectangle(width, height):
    import turtle
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        
        
rectangle(450,200)