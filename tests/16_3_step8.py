""" 
Напишите функцию arithmetic_operation(), 
которая принимает символ одной из четырех арифметических операций (+, -, *, /) 
и возвращает функцию двух аргументов для соответствующей операции.

Примечание 1.
Вызывать функцию arithmetic_operation() не нужно, требуется только реализовать ее.

Примечание 2. 
Модуль operator может быть полезен при решении этой задачи (функции модуля по ссылке).
"""


import operator


def arithmetic_operation(op):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    if op not in ops:
        raise ValueError("Неподдерживаемая операция")
    return ops[op]


add = arithmetic_operation('+')
print(add(10, 20))
