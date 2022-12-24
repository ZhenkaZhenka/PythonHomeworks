# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В решении мы создаем файлы с многочленами и файл с результатом. При каждом запуске пограммы многочлены в файлах заменяются на новые
# Работает только если в обоих файлах находятся многочлены

from random import randint

k1 = int(input('Input first degree: '))
k2 = int(input('Input second degree: '))
nameOfFile1 = 'Task 5, first polynomial.txt'
nameOfFile2 = 'Task 5, second polynomial.txt'
nameOfFile3 = 'Task 5, result polynomial.txt'
mult1stPolynomial = []  # Список с множителями первого многочлена
mult2ndPolynomial = []  # Список с множителями второго многочлена
resultMultipliers = []  # Список с суммой множителей многочленов


def GetPolynomial(k, name):  # Получение и запись многочлена в файл
    with open(name, 'w') as file:
        if k > 1:  # Если введеный коэфициент < 2, то выражение не является многочленом
            while k > 0:
                n = randint(0, 100)
                if k > 1:
                    if n > 0:
                        # получим запись "Nx**k+"
                        file.write(str(n) + 'x**' + str(k) + '+')
                    elif n == 1:
                        # При N = 1 получим запись "x**k+""
                        file.write('x**' + str(k) + '+')
                else:  # Условие для k == 1
                    if n > 0:
                        file.write(str(n) + 'x+')  # Получим запись "Nx+"
                    elif n == 1:
                        file.write('x+')
                k -= 1
            n = randint(0, 100)  # Для k == 0
            if n > 0:
                file.write(str(n))
            file.write('=0')
        else:
            file.write('This is not a polynomial')
        file.write('\n')
    return


def GetResultPolynomial(k, name, list):
    with open(name, 'w') as file:
        if k > 1:  # Если введеный коэфициент < 2, то выражение не является многочленом
            index = 0
            while k > 0:
                n = list[index]
                if k > 1:
                    if n > 0:
                        # получим запись "Nx**k+"
                        file.write(str(n) + 'x**' + str(k) + '+')
                    elif n == 1:
                        # При N = 1 получим запись "x**k+""
                        file.write('x**' + str(k) + '+')
                else:                  # Условие для k == 1
                    if n > 0:
                        file.write(str(n) + 'x+')  # Получим запись "Nx+"
                    elif n == 1:
                        file.write('x+')
                index += 1
                k -= 1
            n = list[index]  # Для k == 0
            if n > 0:
                file.write(str(n))
            file.write('=0')
        else:
            file.write('This is not a polynomial')
        file.write('\n')
    return


# Получение списка из файла, путем разделения слагаемых многочлена
def GetListFromText(nameOfFile, nameOfList):
    with open(nameOfFile, 'r') as file:
        for line in file:
            polynomial = line.split('+')
    return polynomial


# Сложение поиндексно двух списков с множителями
def GetList(mult1stPolynomial, mult2ndPolynomial):
    for i in range(len(mult1stPolynomial)):
        resultMultipliers.append(
            int(mult1stPolynomial[i]) + int(mult2ndPolynomial[i]))
    return resultMultipliers


def GetMultipliers(string):  # Получение множителя путем отсечения не циферной части
    index = 0
    newString = ''
    while string[index].isdigit():
        newString += string[index]
        index += 1
    if not (newString.isdigit()):
        newString = '0'
    return newString


def ChangeList(list):  # Запись множителя в список
    newList = []
    for i in range(len(list)):
        newList.append(int(GetMultipliers(list[i])))
    return newList


# Если у многочленов разные коэфициенты, приравниваем длины списков с множителями для удобства сложения
def IncreaseLengthOfList(list, diff):
    if diff > 0:
        while diff > 0:
            list.insert(0, 0)
            diff -= 1
    return list

#Получение суммы множителей многочленов для записи
def GetResult(mult1stPolynomial, mult2ndPolynomial):
    diff = 0
    if len(mult1stPolynomial) > len(mult2ndPolynomial):
        diff = len(mult1stPolynomial) - len(mult2ndPolynomial)
        mult2ndPolynomial = IncreaseLengthOfList(mult2ndPolynomial, diff)
        list3 = GetList(mult1stPolynomial, mult2ndPolynomial)
    else:
        diff = len(mult2ndPolynomial) - len(mult1stPolynomial)
        mult1stPolynomial = IncreaseLengthOfList(mult1stPolynomial, diff)
        list3 = GetList(mult2ndPolynomial, mult1stPolynomial)
    return list3


GetPolynomial(k1, nameOfFile1)
GetPolynomial(k2, nameOfFile2)

mult1stPolynomial = ChangeList(GetListFromText(nameOfFile1, mult1stPolynomial))
mult2ndPolynomial = ChangeList(GetListFromText(nameOfFile2, mult2ndPolynomial))
resultMultipliers = GetResult(mult1stPolynomial, mult2ndPolynomial)

GetResultPolynomial(len(resultMultipliers) - 1, nameOfFile3, resultMultipliers)
print('Look at files and compare result. Thank you for your attention!')
