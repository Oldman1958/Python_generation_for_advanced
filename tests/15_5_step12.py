""" 
Вам доступен список numbers. 
Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.

Примечание 1. 
Считайте, что список numbers уже объявлен в вашей программе, и вы имеете к нему доступ.

Примечание 2. 
Попробуйте решить задачу двумя способами: с помощью функции reduce() 
и с помощью функций map() и sum().

Примечание 3. 
При решении задачи нужно использовать функции map() и reduce(), написанные в конспекте урока.
"""


numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]


def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result


def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc


res = reduce(lambda x,y: x+y, map(lambda x: x**2, numbers), 0)
print(res)