# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В решении мы создаем файлы с многочленами и файл с результатом. При каждом запуске пограммы многочлены в файлах заменяются на новые
# Работает только если в обоих файлах находятся многочлены

# Нужно добавить сложение многочленов с пропущенными слагаемыми, как Nx**k, при N==0. Мне пришла идея со словарями, надо будет ее опробовать

from random import randint

k1 = int(input('Input first degree: '))
k2 = int(input('Input second degree: '))
nameOfFile1 = 'Task 5, first polynomial.txt'
nameOfFile2 = 'Task 5, second polynomial.txt'
nameOfFile3 = 'Task 5, result polynomial.txt'
mult1stPolynomial = []  # Список с множителями первого многочлена
mult2ndPolynomial = []  # Список с множителями второго многочлена
resPairsPowerMultipliers = {} # Словарь с парами Степень(ключ) - Множитель(значение)


# Получение и запись многочлена в файл
def GetPolynomial(k, name):  
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


#Получение и запись в файл суммы двух многочленов
def GetResultPolynomial(name, resPairsPowerMultipliers):
    key = max(k1, k2)
    with open(name, 'w') as file:
        if key > 1:  # Если введеный коэфициент < 2, то выражение не является многочленом
            index = 0
            while key > 0:
                n = resPairsPowerMultipliers[key]
                if key > 1:
                    if n > 0:
                        # получим запись "Nx**k+"
                        file.write(str(n) + 'x**' + str(key) + '+')
                    elif n == 1:
                        # При N = 1 получим запись "x**k+""
                        file.write('x**' + str(key) + '+')
                else:                  # Условие для k == 1
                    if n > 0:
                        file.write(str(n) + 'x+')  # Получим запись "Nx+"
                    elif n == 1:
                        file.write('x+')
                index += 1
                key -= 1
            n = resPairsPowerMultipliers[key]  # Для k == 0
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

# Получение множителя путем отсечения не циферной части
def GetMultipliers(string):  
    index = 0
    newString = ''
    while string[index].isdigit():
        newString += string[index]
        index += 1
    if not (newString.isdigit()):
        newString = '0'
    return newString

#Получаем ключ, возвращаем интовое значение
def GetKey(string):
    if 'x' in string:
        if string[len(string) - 1] != 'x':
            index = string.index('x')+3   ## 3 символа вправо потому-что "x**", чтоб начать сразу со степени
            key = ''
            while index <= len(string)-1 and string[index].isdigit():
                key += string[index]
                index += 1
        else:
            return 1
    else:
        return 0
    return int(key)

# Создаем соварь с парами Степень(ключ) - Множитель(значение)
def GetDictionary(list):
    for i in range(len(list)):
        key = GetKey(list[i])
        value = int(GetMultipliers(list[i]))
        if key in resPairsPowerMultipliers:
            resPairsPowerMultipliers[key] += value
        else:
            resPairsPowerMultipliers[key] = value


GetPolynomial(k1, nameOfFile1)
GetPolynomial(k2, nameOfFile2)

mult1stPolynomial = GetDictionary(GetListFromText(nameOfFile1, mult1stPolynomial))
mult2ndPolynomial = GetDictionary(GetListFromText(nameOfFile2, mult2ndPolynomial))

GetResultPolynomial(nameOfFile3, resPairsPowerMultipliers)
print('Look at files and compare result. Thank you for your attention!')
