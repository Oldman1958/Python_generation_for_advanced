"""
Почтовый индекс в Латверии имеет вид:

LetterLetterNumber_NumberLetterLetter
где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(),
которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный
Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
"""

import random


def generate_index():
    post_index = ''
    for i in range(7):
        if i == 0 or i == 1 or i == 5 or i == 6:
            post_index += chr(random.randint(65, 90))
        elif i == 2 or i == 4:
            post_index += str(random.randint(0, 99))
        elif i == 3:
            post_index += '_'

    return post_index


# print(generate_index())
