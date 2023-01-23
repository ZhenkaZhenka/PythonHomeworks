import export_contact as ec
import import_contact as ic
import logger as log


def Export():
    print('Do you want to see full contact list or partial contact list?')
    print('"full"\n"partial"')
    data = log.GettingList()
    while True:
        choise = input()
        if choise == 'full':
            return ec.ExportingSortedData(data)
        elif choise == 'partial':
            
            return ec.ExportingSortedData(log.ChoiseOfPitches(data))
        else:
            print('I didnt understand you, plz, try again')



def Start():
    print('What you wanna do: Create new contact or see contacts?')
    print('Input "import" to create new contact or "export" to see contacts or "stop", if you want to stop work')
    while True:
        choise = input()
        if choise == 'import'.lower():
            return ic.ImportData()
        elif choise == 'export'.lower():
            return Export()
        elif choise == 'stop'.lower():
            return
        else:
            print('i didnt understand you, plz, try again')
