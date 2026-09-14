""" 
На вход программе подается Decimal число d. 
Напишите программу, которая вычисляет сумму наибольшей и наименьшей цифры числа d.

Формат входных данных
На вход программе подается десятичное число d.

Формат выходных данных
Программа должна вывести единственное число.
"""

from decimal import Decimal

d = Decimal(input())

# Получаем компоненты
sign, digits, exponent = d.as_tuple()

# digits — это кортеж значащих цифр (без ведущих нулей и без учёта позиции запятой)
# Если число по модулю < 1, значит, в его десятичной записи есть 0 в целой части
all_digits = list(digits)

if abs(d) < 1:
    all_digits.append(0)

max_digit = max(all_digits)
min_digit = min(all_digits)
print(max_digit + min_digit)
