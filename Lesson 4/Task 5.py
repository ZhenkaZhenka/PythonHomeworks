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
list1 = []
list2 = []
list3 = []


def GetPolynomial(k, name):
    with open(name, 'w') as file:
        if k > 1:
            while k > 0:
                n = randint(0, 100)
                if k > 1:
                    if n > 0:
                        file.write(str(n) + 'x**' + str(k) + '+')
                    elif n == 1:
                        file.write('x**' + str(k) + '+')
                else:
                    if n > 0:
                        file.write(str(n) + 'x+')
                    elif n == 1:
                        file.write('x+')
                k -= 1
            n = randint(0, 100)
            if n > 0:
                file.write(str(n))
            file.write('=0')
        else:
            file.write('This is not a polynomial')
        file.write('\n')
    return

def GetResultPolynomial(k, name, list):
    with open(name, 'w') as file:
        if k > 1:
            index = 0
            while k > 0:
                n = list[index]
                if k > 1:
                    if n > 0:
                        file.write(str(n) + 'x**' + str(k) + '+')
                    elif n == 1:
                        file.write('x**' + str(k) + '+')
                else:
                    if n > 0:
                        file.write(str(n) + 'x+')
                    elif n == 1:
                        file.write('x+')
                index += 1
                k -= 1
            n = list[index]
            if n > 0:
                file.write(str(n))
            file.write('=0')
        else:
            file.write('This is not a polynomial')
        file.write('\n')
    return

def GetListFromText(nameOfFile, nameOfList):
    with open(nameOfFile, 'r') as file:
        for line in file:
            polynomial = line.split('+')
    return polynomial

def GetList(list1, list2):
    for i in range(len(list1)):
        list3.append(int(list1[i]) + int(list2[i]))
    return list3

def GetMultipliers(string):
    index = 0
    newString = ''
    while string[index].isdigit():
        newString += string[index]
        index += 1
    return newString
    
def IncreaseLengthOfList(list, diff):
    if diff > 0:
        while diff > 0:
            list.insert(0,0)
            diff -= 1
    return list

def ChangeList(list):
    newList = []
    for i in range(len(list)):
        newList.append(GetMultipliers(list[i]))
    return newList

def GetResult(list1, list2):
    diff = 0
    if len(list1) > len(list2):
        diff = len(list1) - len(list2)
        list2 = IncreaseLengthOfList(list2, diff)
        list3 = GetList(list1, list2)
    else:
        diff = len(list2) - len(list1)
        list1 = IncreaseLengthOfList(list1, diff)
        list3 = GetList(list2, list1)
    return list3


GetPolynomial(k1, nameOfFile1)
GetPolynomial(k2, nameOfFile2)
list1 = ChangeList(GetListFromText(nameOfFile1, list1))
list2 = ChangeList(GetListFromText(nameOfFile2, list2))

try:
    list3 = GetResult(list1, list2)
    GetResultPolynomial(len(list3) - 1, nameOfFile3, list3)
    print('Look at files and compare result. Thank you for your attention!')
except:
    print("One of the files doesn't contain polynomial")
