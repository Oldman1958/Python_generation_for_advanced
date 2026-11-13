""" 
Pretty print
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.

Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'.

Примечание 1. 
Вызывать функцию pretty_print() не нужно, требуется только реализовать ее.

Примечание 2. 
Cчитайте, что side и delimiter состоят всегда из одного символа.
"""


def pretty_print(data, side='-', delimiter='|'):
    
    row = f' {delimiter} '.join(map(str, data))
    width = len(row) + 4
    print(side * width)
    print(f'{delimiter} {row} {delimiter}')
    print(side * width)



pretty_print([1, 2, 10, 23, 123, 3000])
