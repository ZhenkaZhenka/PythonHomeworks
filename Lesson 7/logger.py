from datetime import datetime as dt

def GettingList():
    list = []
    with open('Phone book.txt', 'r') as file:
        for line in file:
            list.append(line.split())
    return list

def SortingList(data):
    print('Do you want to sort it?')
    sort = input('Input pitch that you want to use as base, " "-if you dont want to sort: ')
    match(sort):
        case 'id':
            return sorted(LogSortedExport(data, sort), key = lambda x: int(x[0]))
        case 'surname':
            return sorted(LogSortedExport(data, sort), key = lambda x: x[1])
        case 'name':
            return sorted(LogSortedExport(data, sort), key = lambda x: x[2])
        case 'phone number':
            return sorted(LogSortedExport(data, sort), key = lambda x: x[3])
        case 'comment':
            return sorted(LogSortedExport(data, sort), key = lambda x: x[4])
        case _:
            return LogExport(data)

def ChoiseOfPitches(data):
    print('Choose the points that you want to see: ')
    dict = {'id': 0, 'surname': 1, 'name': 2, 'number': 3, 'comment': 4}
    print('Input the pitches via " " that you whant to see : ')
    global list 
    list = input().split()
    newList = []
    for i in LogChoosenPitches(data):
        subList = []
        for j in list:
            if j in dict.keys():
                subList.append(i[dict[j]])
        newList.append(subList)
    return newList

def LogImport(data):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} {} has been added\n'.format(time, ' '.join(data)))
    return data

def LogExport(data):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} Somebody looked at your contact list\n'.format(time))
    return data

def LogSortedExport(data, key):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} Somebody looked at your sorted by {} contact list\n'.format(time, key))
    return data

def LogChoosenPitches(data):
    pitches = ' '.join(list)
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} Somebody looked at pitches {} in your contact list\n'.format(time, pitches))
    return data
