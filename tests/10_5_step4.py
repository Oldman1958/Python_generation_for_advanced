""" 
В чем отличие ❓
Напишите функцию dict_diff(), которая принимает два аргумента в следующем порядке:

data1 – первый словарь
data2 – второй словарь
Функция должна возвращать словарь – результат сравнения словаря data1 относительно словаря data2. 
В результирующем словаре ключами будут ключи из переданных словарей, 
а значениями – строки с описанием отличий:

'added' – ключ отсутствует в первом словаре и присутствует во втором
'deleted' – ключ присутствует в первом словаре и отсутствует во втором
'changed' – ключ присутствует и в первом, и во втором словарях, но значения отличаются
'unchanged' – ключ и значение находятся без изменений и в первом, и во втором словарях

Примечание 1. Порядок элементов в результирующем словаре не учитывается.

Примечание 2. Вызывать функцию dict_diff() не нужно, требуется только реализовать ее.
"""


def dict_diff(data1, data2):
    res = {}
    for key, value in data1.items():
        if key not in data2:
            res[key] = 'deleted'
        elif key in data2:
            if data2[key] == data1[key]:
                res[key] = 'unchanged'
            elif data1[key] != data2[key]:
                res[key] = 'changed'
    for key, value in data2.items():
        if key not in data1:
            res[key] = 'added'   
    return res


data1 = {'one': 1, 'two': 2, 'four': 4}
data2 = {'two': 2.5, 'three': 3, 'four': 4}
print(dict_diff(data1, data2))

data1 = {'one': 1, 'two': 2, 'four': 4}
data2 = {'four': 4}
print(dict_diff(data1, data2))
