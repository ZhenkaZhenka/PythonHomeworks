# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import math

number = int(input('Input number transform it to binary form: '))
binaryNumber = []

while number != 0:
    if number % 2 == 1:
        binaryNumber.insert(0, '1')
    else:
        binaryNumber.insert(0, '0')
    number = int(number / 2)

binNum = ''.join(binaryNumber)

print('After transformation to binary form number got form: ' + '\n' + binNum)
