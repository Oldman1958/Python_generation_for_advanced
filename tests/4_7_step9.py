"""
Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах,
затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""

n, m = map(int, input().split())

matrix_1 = []
matrix_2 = []

for i in range(n):
    matrix_1.append(list(map(int, input().split())))

input()

for i in range(n):
    matrix_2.append(list(map(int, input().split())))

matrix_result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_result[i][j] = matrix_1[i][j] + matrix_2[i][j]
        print(matrix_result[i][j], end=' ')
    print()

