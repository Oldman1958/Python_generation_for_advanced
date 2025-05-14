"""
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые nn строк треугольника Паскаля.
"""
from math import factorial as f


def str_Pascal(n):
    s = []
    for m in range(n + 1):
        k = f(n) / (f(m) * f(n - m))
        s.append(int(k))
    return s


a = int(input())
for i in range(a):
    print(*str_Pascal(i), end='\n')
