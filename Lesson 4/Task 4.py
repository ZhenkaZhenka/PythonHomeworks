# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Input degree: '))

with open ("Task 4.txt", 'a') as file:
    if k > 1:
        while k > 0:
            n = randint(0, 100)
            if k > 1:
                if n > 0:
                    file.write(str(n) + 'x**' + str(k))
                elif n == 1:
                    file.write('x**'+ str(k))
                file.write('+')
            else:
                if n > 0:
                    file.write(str(n) + 'x')
                elif n == 1:
                    file.write('x')
                file.write('+')
            k -= 1
        n = randint(0, 100)
        if n > 0:
            file.write(str(n))
        file.write('=0')
    else:
        file.write('This is not a polynomial')
    file.write('\n')

print('Look at file')
    