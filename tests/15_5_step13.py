""" 
Вам доступен список numbers. 
Напишите программу для вычисления и вывода суммы квадратов двузначных чисел из списка numbers, 
которые делятся на 7 без остатка.

Примечание 1. 
Считайте, что список numbers уже объявлен в вашей программе, и вы имеете к нему доступ.

Примечание 2. 
При решении задачи нужно использовать функции filter() и map(), написанные в конспекте урока.

Примечание 3. 
На 7 должно делиться исходное двузначное число, а не его квадрат.

Примечание 4. 
Двузначные числа могут быть как положительными (например, 13), 
так и отрицательными (например, -56).
"""


numbers = [14, 15, -1, 2, 0, -42, 36, 2]


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
            result.append(item)
    return result

# Условие для двузначного числа: от -99 до -10 или от 10 до 99


def is_two_digit(x):
    return (10 <= abs(x) <= 99)

# Условие: делится на 7 без остатка


def is_divisible_by_7(x):
    return x % 7 == 0


# Сначала отбираем двузначные числа, которые делятся на 7
filtered = filter(lambda x: is_two_digit(x) and is_divisible_by_7(x), numbers)

# Затем возводим их в квадрат
squared = map(lambda x: x ** 2, filtered)

# Считаем сумму квадратов
result = sum(squared)
print(result)
