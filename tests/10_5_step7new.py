""" 
Функция scrabble() 
Напишите функцию scrabble(), которая принимает два аргумента в следующем порядке:

letters – строка, содержащая произвольный набор букв
word – строка, содержащая слово
Функция должна возвращать True, если из переданного набора букв letters 
можно составить указанное слово word, или False в противном случае.

Примечание 1. 
При проверке учитывается количество символов, которые нужны для составления слова, 
и не учитывается их регистр.

Примечание 2. 
Для составления слова необязательно использовать все буквы из переданного набора.

Примечание 3. 
Вызывать функцию scrabble() не нужно, требуется только реализовать ее.
"""


def scrabble(letters, word):
    from collections import Counter
    count_letters = Counter(letters.lower())
    count_word = Counter(word.lower())
    for letter, val in count_word.items():
        if letter not in count_letters or count_letters[letter] < val:
            return False
    return True


print(scrabble('BEEGEEK', 'geekbee'))
print(scrabble('othpyn', 'Python'))
print(scrabble('bababa', 'BBBAAAccc'))
