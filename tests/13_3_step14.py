""" 
Сопряженные числа
Даны натуральное число n и два комплексных числа z1 и z2.
Напишите программу, которая вычисляет и выводит значение выражения:

(Ищите выражение сами, вводить эту ересь сложно :))
"""
n = int(input())
z1 = complex(input())
z2 = complex(input())

z1_conj = z1.conjugate()
z2_conj = z2.conjugate()

result = z1 ** n + z2 ** n + z1_conj ** n + z2_conj ** (n + 1)

print(result)
