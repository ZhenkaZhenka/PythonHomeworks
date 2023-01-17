# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
import random

firstList = list(enumerate(random.sample(range(-15, 20), 10)))
minValue = int(input('Input min value to filter: '))
maxValue = int(input('Input max value to filter: '))

print(list(x[1] for x in firstList))

filteredList = list(filter(lambda x: x[1] >= minValue and x[1] <= maxValue, firstList))

indexList = [x[0] for x in filteredList]

print(indexList)
