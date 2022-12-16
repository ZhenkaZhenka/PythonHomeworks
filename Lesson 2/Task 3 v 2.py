# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:
# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

number = int(input('Input size of dictionary: '))

dict = {}

for i in range(1, number+1):
    dict.setdefault(i, (round((1+1/i)**i,2)))

print(dict)