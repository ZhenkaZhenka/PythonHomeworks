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

## Показывает все оценки выбранного ученика
def ShowEvaluationsOfOneStudent():
    name = CheckTheName('Input name of student to see evaluations:')
    if name == None:
        print('you didnt want to fill in name of student')
        return
    temp_list = id.GettingList('List of subjects')
    temp_dict = {}
    for i in temp_list:
        temp_dict2 = id.GetDictOfNames(i)
        temp_dict[i] = temp_dict2[name]
        temp_dict2.clear()
    print('Evaluations of', name.replace(':', ' '), 'in every subjects are:')
    for i in temp_dict.keys():
        print('{}: {}'.format(i, temp_dict[i]))
    return

def Export():
    print('At this moment i can suggest to you watch at:\n*List of students\n*Evaluations of student')
    temp = input()
    match temp:
        case 'List of students': ShowStudents()
        case 'Evaluations': ShowEvaluationsOfOneStudent()
        case _: print('i didnt get your choise')
    return
