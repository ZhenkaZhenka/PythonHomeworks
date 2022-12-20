# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import math

number = int(input('Input size of the list: '))

list = [0] * number
resultList = []

for i in range(0, number):
    list[i] = random.randint(0, 10)

for i in range(0, math.ceil(len(list)/2)):
    resultList.append(list[i] * list[int(len(list) - 1 - i)])

print('Input list is:')
print(list)
print('Result of the multiply of needed pairs is:')
print(resultList)
