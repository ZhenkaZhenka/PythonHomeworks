# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = input('Input number of quarter: ')

def Main(number):
    match(number):
        case '1': print('Coordinates of this quarter are X > 0, Y > 0')
        case '2': print('Coordanates of this quarter are X < 0, Y > 0')
        case '3': print('Coordinates of this quarter are X < 0, Y > 0')
        case '4': print('Coordinates of this quarter are X > 0, Y < 0')
        case 'center': print('Coordinates of this point are X = 0, Y = 0')
        case _: print('This is not a part of coordiante system')
    return

Main(number)