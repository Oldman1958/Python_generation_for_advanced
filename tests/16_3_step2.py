""" 
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   
    # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i

    return result

                  
Примечание 1. 
Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter() и reduce(), однако лучше сделать это задание честно. 😃

Примечание 2. 
Вызывать функцию product_of_odds() не нужно, требуется только реализовать ее в функциональном стиле.
"""

from functools import reduce


def product_of_odds(data):
    odds = filter(lambda x: x % 2 == 1, data)
    return reduce(lambda acc, x: acc * x, odds, 1)


print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
