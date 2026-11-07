""" 
Вам доступны списки countries, capitals и population. 
Используя параллельную итерацию сразу по трем спискам countries, capitals и population, 
выведите информацию о стране в следующем формате:

<capital> is the capital of <country>, population equal <population> people.

Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.
...
                  
Для каждой страны информацию нужно выводить на отдельной строке.

Примечание. 
Считайте, что списки countries, capitals и population уже объявлены в вашей программе, 
и вы имеете к ним доступ.
"""


countries = ['Australia', 'Canada', 'Portugal', 'Japan']
capitals = ['Canberra', 'Ottawa', 'Lissabon', 'Tokyo']
population = [27_840_775, 41_575_585, 10_749_635, 122_950_000]

for x, y, z in zip(countries, capitals, population):
    print(f"{y} is the capital of {x}, population equal {z} people.")
