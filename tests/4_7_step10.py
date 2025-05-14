"""
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице,
затем элементы первой матрицы, затем пустая строка.
Далее следуют числа m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""

n, m = map(int, input().split())

matrix_1 = []
matrix_2 = []

for i in range(n):
    matrix_1.append(list(map(int, input().split())))

input()

m, k = map(int, input().split())
for i in range(m):
    matrix_2.append(list(map(int, input().split())))

matrix_result = [[0 for _ in range(n)] for _ in range(n)]

"""
Чего-то наговнокодил, так и не разобрался чего. Надо взять отпуск на недельку...
for i in range(n):
    for j in range(m):
        sum_mpl = 0
        # matrix_result[i][j] = matrix_1[i][j] + matrix_2[i][j]
        # print(matrix_result[i][j], end=' ')
        for el in range(m):
            sum_mpl += matrix_1[i][j] * matrix_2[el][j]
        matrix_result[i][j] = sum_mpl
        print(matrix_result[i][j], end=' ')

    print()
Ниже решение не мое - списал честно.
"""
for i in range(n):
    for j in range(k):
        el = 0
        for r in range(m):
            el += matrix_1[i][r] * matrix_2[r][j]
        matrix_result[i][j] = el

for row in matrix_result:
    print(*row)
