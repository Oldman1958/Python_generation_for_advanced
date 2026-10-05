""" 

"""

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


field_index = int(input()) - 1  # преобразуем 1–4 в индекс 0–3

# Без условных операторов: используем кортеж индексов для key
# Но здесь достаточно просто взять индекс: athletes сортируются по athletes[i][field_index]

sorted_athletes = sorted(athletes, key=lambda x: x[field_index])

for athlete in sorted_athletes:
    print(*athlete)
