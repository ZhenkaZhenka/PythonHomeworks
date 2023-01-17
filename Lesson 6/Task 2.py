# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
from random import randint

arr = [randint(-10, 15) for i in range(21)]

minValue = int(input('Input min value to filter: '))
maxValue = int(input('Input max value to filter: '))
print(arr)
resList = list(filter(lambda x: x <= maxValue and x >= minValue, arr))
print(resList)
