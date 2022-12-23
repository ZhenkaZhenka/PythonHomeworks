# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Формулировка размытая, как мне показалось
# Можно было сделать через встроеные функции, но я этим не воспользовался

from random import randint 

size = int(input('Input size of the list: '))
maxRandNumber = int(input('Input maxmal random number: '))

list = []
tempList = [0] * (maxRandNumber+1)
resultList = []
setOfNumbers = []

# Здесь я генерирую исходный лист
for i in range(size):
    list.append(randint(0, maxRandNumber))

# Здесь я считаю повторения числа в изначальном листе
for i in list:
    tempList[i] += 1

# Если число в листе появляется только один раз, то я добавляю индекс этого места в листе как число, 
# которое есть в изначальном листе
for i in range(len(tempList)):
    if 2 > tempList[i] > 0:
        resultList.append(i)

# Здесь я получаю множество чисел
for i in range(len(tempList)):
    if tempList[i] > 0:
        setOfNumbers.append(i)

print('Input list is:')
print(list)
print('List of non-repeating numbers in the input list is:')
print(resultList)
print('Set of the numbers in list is: ')
print(setOfNumbers)