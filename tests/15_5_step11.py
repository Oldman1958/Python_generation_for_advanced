""" 
Вам доступен список numbers. 
Напишите программу, которая с помощью функций filter() и map() 
отбирает из заданного списка numbers трехзначные числа, 
дающие при делении на 5 остаток 2, и выводит их кубы, каждый на отдельной строке.

Примечание 1. 
Считайте, что список numbers уже объявлен в вашей программе, и вы имеете к нему доступ.

Примечание 2. 
При решении задачи нужно использовать функции filter() и map(), написанные в конспекте урока.
"""

numbers = [854, 10, 5, 452, 478, 236, 202, 41]


def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            # добавляем элемент item если функция function вернула значение True
            result.append(item)

    return result


def is_case(x):
    return len(str(x)) == 3 and x % 5 == 2


result = map(lambda x: x**3, filter(is_case, numbers))

print(*result, sep='\n')