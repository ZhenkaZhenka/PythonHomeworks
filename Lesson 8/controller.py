import import_data as id
import export_data as ed

def Start():
    print('Hello, what do you want to do?')
    print('import, if you want to add somesthing\nexport, if you want to see something\n')
    temp2 = True
    while temp2:
        temp = input('*import\n*export\n')
        match temp:
            case 'import': id.Import()
            case 'export': ed.Export()
            case 'stop': temp2 = False
            case _: print('I didnt catch you, can you try again?')
    print('Have a good day!')
    return