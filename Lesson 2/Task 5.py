# Реализуйте алгоритм перемешивания списка.

import random

set_ok = False

while(set_ok != True):
    try:
        number = int(input('Input size of array: '))
        set_ok = True
    except:
        print('Input a number, not a string')

list = [i for i in range(0, number)]

print("Input array:")
print(list)

for i in list:
    index = random.randint(0, len(list)-1)
    temp = list[i]
    list[i] = list[index]
    list[index] = temp

print('The array was messed up and got the form:')
print(list)