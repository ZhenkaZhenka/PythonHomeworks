# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

number = int(input('Input size of array: '))
maxFrac = 0
minFrac = 0.99

list = []

for i in range(0, number):
    list.append(round(random.uniform(0.0, 10.0), 2))

for i in list:
    if i - int(i) > maxFrac:
        maxFrac = i - int(i)
    if i - int(i) < minFrac:
        minFrac = i - int(i)

print('Input list is:')
print(list)
print('Difference between maximal fractional part and minimal fractional part is: ')
print(round(maxFrac - minFrac, 2))
