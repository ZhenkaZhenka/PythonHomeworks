#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#  Пример:
#  - 6782 -> 23
#  - 0,56 -> 11

set_ok = False

def GetNumber(set_ok):
    while(set_ok != True):
        try:
            number = float(input('Input real number: '))
            set_ok = True
        except:
            print('Input a number, not a string')
    return number

number = GetNumber(set_ok)

summ_of_number = 0

while (number % 10 != 0):
    number *= 10

while(int(number) != 0):
    summ_of_number += (int(number) % 10)
    number /= 10

print(summ_of_number)
