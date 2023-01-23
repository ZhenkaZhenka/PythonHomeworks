import logger as log

def CheckId():
    data = log.GettingList()
    idList = []
    for i in data:
        idList.append(i[0])
    while True:
        try:
            id = input('Input ID number of contact: ')
            if id in idList:
                e
            else:
                return id
        except Exception as e:
            print('This id already exist, try again')


def GetData():
    id = CheckId()
    surname = input('Input surname: ')
    name = input('Input name: ')
    number = input('Input phone number: ')
    comment = input('Fill in comment for contact: ')
    list = [id, surname, name, number, comment]
    return list

def ImportData():
    data = GetData()
    with open('Phone book.txt', 'a') as file:
        file.write(' '.join(log.LogImport(data)))
        file.write('\n')
    print('Imports succesful')
    return 
