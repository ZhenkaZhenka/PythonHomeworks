# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Input X coordinate: '))
y = int(input('Input Y coordinate: '))

dict = {
    x > 0 and y > 0: 'This point is located in a first quarter',
    x < 0 and y > 0: 'This point is located in a second quarter',
    x < 0 and y < 0: 'This point is located in a third quarter',
    x > 0 and y < 0: 'This point is located in a fourth quarter',
    x == 0 and y != 0: 'This point is located on the X coordinate line',
    x != 0 and y == 0: 'This point is located on the Y coordinate line',
    x == 0 and y == 0: 'This point is a center of the coordiante system'
}

print('Input coordanates are: X=',x,' Y=',y,':',dict.get(True))
