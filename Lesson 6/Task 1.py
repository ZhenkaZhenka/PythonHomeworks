# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

firstNumber = int(input('Input first number in list: '))
step = int(input('Input multiplier: '))
size = int(input('Inputsize of the list: '))

resList = [firstNumber + (x - 1)*step for x in range(size)]

print(resList)