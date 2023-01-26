## Импорт данных
from random import randint


## Получаем лист имен и фамилий, в каждый новый учебный предмет будет добавлять список из имеющихся имен
def GettingList(name_of_file):
    list = []
    with open('{}.txt'.format(name_of_file), 'r') as file:
        for line in file:
            list.append(line.replace('\n', ''))
    return list

## Добавление нового имени ученика в список
def GetNewName():
    name = input('Input student name in form "Surname Name": \n').replace(' ', ':')
    with open('List of students.txt', 'a') as file: # Добавляем нового ученика в файл со списком всех студентов
        file.write(name + '\n')
    temp_list = GettingList('List of subjects')
    for i in temp_list: # Добавляем нового ученика в каждый файл с предметом
        with open('{}.txt'.format(i), 'a') as file:
            file.write(name + '\n')
    print('Import successful')
    return

## ДОбавление нового учебного предмета и создание файла
def GetSubject():
    subject = CheckSubject('This subject already exist', True)
    if subject == None:
        print('you didnt want to create new subject')
        return
    listOfStudents = GettingList('List of students')
    with open('{}.txt'.format(subject), 'a') as file:# Создаем файл с предметом и вписываем туда всех учеников
        for i in listOfStudents:
            file.write(i)
            file.write('\n')
    with open('List of subjects.txt', 'a') as file:# Добавляем имя нового предмета в файл со списков предметов
        file.write('\n' + subject)
    print('Import successful')
    return

## Проверка наличия предмета, чтоб не повторяться
def CheckSubject(message, marker):
    while True:
        try:
            subject = input('Input name of subject:\n')
            temp_list = []
            with open('List of subjects.txt', 'r') as file:
                for line in file:
                    temp_list.append(line.replace('\n', ''))## Создаем лист из названий предметов
            print(temp_list)
            if marker:## Если marker == True, то выполняется проверка на наличие школьного предмета
                if not subject in temp_list:
                    return subject
                else:
                    e
            else:## Если marker == False, то проверяется отсутствие школьного предмета
                if not subject in temp_list:
                    e
                else:
                    return subject
        except Exception as e:
            print(message)
            stop = input('If you decide to stop operation, print "stop"\n')
            if stop == 'stop':
                return


## Метод получения списка учеников и их оценок для добавления оценки
def GetDictOfNames(nameOfSubject):
    dictToWork = {}
    with open('{}.txt'.format(nameOfSubject), 'r') as file:
        for line in file:
            temp_list = line.split()# Разделяем строки в файлах на имена и оценки для удобства работы
            if len(temp_list) == 2: #Если оценок нет, то temp_list будет иметь только одно поле
                dictToWork[temp_list[0].replace('\n', '')] = temp_list[1]
            else:
                dictToWork[temp_list[0].replace('\n', '')] = ''
    return dictToWork

## Проверка наличия имени и фамилии в словаре
def CheckKey(dict):
    while True:
        try:
            name = input('Input name of student:\n').replace(' ', ':')
            if name in dict.keys():
                return name
            else:
                e
        except Exception as e:
            print('You dont have student with this name or you was mistaken in input')

## Добавление оценки ученику по предмету
def AddEvaluation():
    subject = CheckSubject('You dont have this subject, be accurate', False)# Ввод предмета и проверка на наличие такового
    if subject == None:
        print('you have stopped operation')
        return
    tempDict = GetDictOfNames(subject)# Создаем словарь, где ключи это имена учеников а значения - оценки
    name = CheckKey(tempDict)# Ввод имени ученика и проверка на наличие такового
    tempDict[name] = str(tempDict[name]) + input('Input evaluation\n') + ',' # Оценки вводятся string, в файл идут все оценки, которые получает ученик
    with open('{}.txt'.format(subject), 'w') as file:
        for i in tempDict:
            file.write(str(i) + ' ' + str(tempDict[i]) + '\n')# Перезапись всего файла
    print('Import successful')
    return


## Добавление 5 слуйчайных оценок каждому ученику по каждому предмету
def AddRandEvaluation(subject, name):
    tempDict = GetDictOfNames(subject)
    for i in range(6):
        evaluation = randint(1,5)
        tempDict[name] = str(tempDict[name]) + str(evaluation) + ','
    with open('{}.txt'.format(subject), 'w') as file:
        for i in tempDict:
            file.write(str(i) + ' ' + str(tempDict[i]) + '\n')
    return

def ImportRandomEval():
    tempListOfSubjects = GettingList('List of subjects')# Формируем список предметов
    tempListOfStudents = GettingList('List of students')# Формируем список учеников
    for i in tempListOfStudents:# Каждому ученику
        for j in tempListOfSubjects:# По каждому предмету
            AddRandEvaluation(j, i)# Генерация и добавление оценки
    print('Import successful')
    return

def Import():
    print('What do you want to add?\n1.Subject\n2.Student\n3.Evaluation\n4.RandEvaluation\n5.Stop working')
    print('Input "5.RandEvaluation" to add 5 random values to every student in every subject')
    temp = input()
    match temp:
        case '1': GetSubject()# Добавить новый предмет
        case '2': GetNewName()# Добавить ученика
        case '3': AddEvaluation()# Поставить оценку ученику по нужному предмету
        case '4': ImportRandomEval()# Поставить каждому ученику по 5 случайных оценок по всем предметам
        case '5': return# Остановить работу и выйти в главное меню
        case _: print('I didnt understand you, try again or input "stop"')
    return