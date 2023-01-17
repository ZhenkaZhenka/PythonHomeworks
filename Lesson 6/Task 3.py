# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

number = int(input('Input number to raise it to a power: '))
power = int(input('Input power for number: '))

def Recursion(number, power):
    if power == 1: return number
    else: 
        return number * Recursion(number, power-1)

print(Recursion(number, power))