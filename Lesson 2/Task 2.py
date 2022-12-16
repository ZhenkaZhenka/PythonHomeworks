# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Input N: '))


def Factorial(number):
    if number == 0:
        return 1
    else:
        return number * Factorial(number - 1)


list = [Factorial(n) for n in range(1, number+1)]

print(list)
