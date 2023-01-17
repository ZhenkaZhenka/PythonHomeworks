# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
import random

firstList = list(enumerate(random.sample(range(-5, 5), 10)))
minValue = int(input('Input min value to filter: '))
maxValue = int(input('Input max value to filter: '))

print(firstList)

filteredList = list(filter(lambda x: x[1] >= minValue and x[1] <= maxValue, firstList))

print(filteredList)

indexList = [x[0] for x in filteredList]

print(indexList)
