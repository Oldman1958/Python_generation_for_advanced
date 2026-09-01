""" 
Самое редкое слово 🌶️
На вход программе подается строка текста. 
Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. 
Программа не должна быть чувствительной к регистру, 
слова apple и Apple должна воспринимать как одинаковые.

Примечание 2. 
Слово – последовательность букв. 
Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, 
которые нужно игнорировать. Других символов в тексте нет.
"""



import re
from collections import Counter

text = input()

# Извлекаем слова (только буквы), приводим к нижнему регистру
words = re.findall(r'[a-za-яё]+', text.lower())

# Считаем частоты
counts = Counter(words)

# Находим минимальную частоту
min_freq = min(counts.values())

# Среди слов с минимальной частотой выбираем лексикографически наименьшее
result = min(filter(lambda w: counts[w] == min_freq, counts.keys()))

print(result)

""" 
London is the capital of Great Britain. 
More than six million people live in London. 
London lies on both banks of the river Thames. 
It is the largest city in Europe and one of the largest cities in the world. 
London is not only the capital of the country, 
it is also a very big port, one of the greatest commercial centres in the world, 
a university city, and the seat of the government of Great Britain!
"""