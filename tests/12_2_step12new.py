""" 
Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, 
состоящих из строчных и прописных английских букв и цифр, кроме тех, 
которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: 
в каждом пароле обязательно должна присутствовать хотя бы одна цифра 
и как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести n паролей длиной m символов в соответствии с условием задачи, 
каждый на отдельной строке.

Примечание 1. 
Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. 
Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, 
состоящий из count случайных паролей длиной length символов.

Примечание 3. 
Приведенные ниже тесты – это лишь примеры ответа. 
Возможны и другие варианты генерации паролей.
"""

import random


def generate_password(length: int):
    lowercase = "abcdefghijkmnpqrstuvwxyz"  # без l и o
    uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # без I и O
    digits = "23456789"                      # без 0 и 1
    all_chars = lowercase + uppercase + digits

    # Гарантируем минимум по одному символу каждого типа
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]

    # Остальные символы — случайные из всего набора
    password_chars += [random.choice(all_chars) for _ in range(length - 3)]
    random.shuffle(password_chars)

    return ''.join(password_chars)


def generate_passwords(count: int, length: int):
    return [generate_password(length) for _ in range(count)]


n = int(input())
m = int(input())

for pwd in generate_passwords(n, m):
    print(pwd)
