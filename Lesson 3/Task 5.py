# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 2

number = int(input('Input an amount of the row of Fibonachi to both directions: '))
fibRow = []


def Fib(number): # Я решил объеденить два метода в один, на сколько это правильно?
    if number >= 0:
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return Fib(number - 1) + Fib(number - 2)
    else:
        if number == 1:
            return 1
        else:
            return Fib(number + 2) - Fib(number + 1)


for i in range(0, number+1):
    fibRow.append(Fib(i))
    fibRow.insert(0, Fib(-i))

fibRow.remove(0) #повторял 0 в листе, я не придумал ничего лучшего, чем это
print('Fibbonachi row is:')
print(fibRow)
