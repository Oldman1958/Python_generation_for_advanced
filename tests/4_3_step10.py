"""
На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника Паскаля в
виде списка (нумерация строк начинается с нуля).
"""
from math import factorial as f


def str_Pascal(n):
    s = []
    for m in range(n + 1):
        k = f(n) / (f(m) * f(n - m))
        s.append(int(k))
    return s


a = int(input())
print(str_Pascal(a))
