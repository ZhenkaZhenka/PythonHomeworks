# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

AX = int(input('Input X coordinate of A point: '))
AY = int(input('Input Y coordinate of A point: '))
BX = int(input('Input X coordinate of B point: '))
BY = int(input('Input Y coordinate of B point: '))

def Distance(AX, AY, BX, BY):
    return math.sqrt((BX - AX) ** 2 + (BY - AY) ** 2)

print('Distance between A and B points is ', round(Distance(AX, AY, BX, BY),2))
