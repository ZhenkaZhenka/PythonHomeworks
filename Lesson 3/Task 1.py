# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

number = int(input('Input size of list: '))

result = 0

list = []

for i in range(0, number):
    list.append(random.randint(0, 10))

for i in range(1, len(list), 2):
    result += list[i]

print(list)
print('Summ of the numbers in the list placed in odd pisitions is: ' + str(result))