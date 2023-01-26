## Здесь мы будем работать с экспортом данных для пользователя

import import_data as id

def CheckTheName(message):
    temp_list = id.GettingList('List of students')
    while True:
        try:
            print(message)
            name = input()
            if name.replace(' ', ':') in temp_list:
                return name.replace(' ', ':')
            else:
                e
        except Exception as e:
            print('You dont have that student')
            stop = input('If you decide to stop operation, print "stop"\n')
            if stop == 'stop':
                return

# Показывает список всех студентов
def ShowStudents():
    tempList = []
    with open('List of students.txt', 'r') as file:
        for line in file:
            tempList.append(line.replace(':', ' ').replace('\n', ''))
    for i in tempList:
        print(i)
    print('Export successful')
    return

## Формирует словарь с оценками выбранного ученика
def GetEvaluationsOfOneStudent(name, marker):
    temp_list = id.GettingList('List of subjects')
    temp_dict = {}
    for i in temp_list:
        temp_dict2 = id.GetDictOfNames(i)
        if marker: # Если marker == True, то выводятся все оценки ученика
            temp_dict[i] = temp_dict2[name]
        else:       #Если marker == False, то выводится средняя оценка ученика по каждому предмету
            temp_dict[i] = GetMiddleEvaluaton(temp_dict2[name])
        temp_dict2.clear()
    return temp_dict


# Метод с выводом оценок выбранного ученика
def ShowEvaluationsOfOneStudent(marker):
    name = CheckTheName('Input name of student to see evaluations:')
    if name == None:
        print('you didnt want to fill in name of student')
        return
    temp_dict = GetEvaluationsOfOneStudent(name, marker)
    if marker:
        print('Evaluations of', name.replace(':', ' '), 'in every subjects are:')
    else:
        print('Middle valuations of', name.replace(':', ' '), 'in every subjects are:')
    for i in temp_dict.keys():
        print('{}: {}'.format(i, temp_dict[i]))
    return


##Считает среднюю оценку ученика
def GetMiddleEvaluaton(string):
    list = string.split(',')
    sum = 0
    for i in range(len(list)-1):
        sum += int(list[i])
    return round(sum/(len(list)-1), 2)

## Показывает среднюю оценку каждого ученика по выбраному предмету
def ShowMiddleEvaluationInSubject():
    nameOfSubject = id.CheckSubject('You dont have this subject, be accurate', False)
    temp_dict = id.GetDictOfNames(nameOfSubject)
    for i in temp_dict.keys():
        temp = temp_dict[i]
        temp_dict[i] = GetMiddleEvaluaton(temp)# Разница
    print('Middle evaluations of every student in', nameOfSubject, 'are:')
    for i in temp_dict.keys():
        print('{}\t{}'.format(i, temp_dict[i]))
    return



def Export():
    print('At this moment i can suggest to you watch at:')
    print('1.List of students')
    print('2.Evaluations of one students')
    print('3.Middle evaluations of one student')
    print('4.Middle evaluations of every student in one subject')
    temp = input()
    match temp:
        case '1': ShowStudents()
        case '2': ShowEvaluationsOfOneStudent(True)
        case '3': ShowEvaluationsOfOneStudent(False)
        case '4': ShowMiddleEvaluationInSubject()
        case _: print('i didnt get your choise')
    return