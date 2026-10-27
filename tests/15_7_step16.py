""" 
Вам доступен список data, содержащий информацию о городах в виде списков. 
Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() 
выводит в алфавитном порядке список primary городов с населением более 10000000 человек, в формате:

Cities: Beijing, Buenos Aires, ...

                  
Примечание 1. 
Считайте, что список data уже объявлен в вашей программе, и вы имеете к нему доступ.

Примечание 2. 
Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter(), map(), sorted() и reduce(), 
однако лучше сделать это задание честно. 😃

Примечание 3. 
Ставить запятую в конце вывода не нужно.
"""

from functools import reduce

data = [
    ['Bangkok', 18180280, 'admin'],
    ['Karachi', 21422590, 'primary'],
    ['Bengaluru', 13187098, 'primary'],
]

# 1. filter: оставляем только primary города с населением > 10 000 000
filtered = filter(lambda city: city[2] ==
                  'primary' and city[1] > 10_000_000, data)

# 2. map: извлекаем только названия городов
cities = map(lambda city: city[0], filtered)

# 3. sorted: сортируем названия в алфавитном порядке
sorted_cities = sorted(cities)

# 4. reduce: собираем строку вида "Beijing, Buenos Aires, ..."
if sorted_cities:
    result = reduce(lambda acc, name: f"{acc}, {name}", sorted_cities)
    print(f"Cities: {result}")
else:
    print("Cities: ")
