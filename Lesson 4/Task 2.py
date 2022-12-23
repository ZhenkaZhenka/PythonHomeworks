# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Input number: '))

list = []

for i in range(2, number+1, 1):
    while number % i == 0:
        if int(number) % i == 0:
            list.append(str(i))
            number /= i

print('The number consists of a product : ' + '*'.join(list))