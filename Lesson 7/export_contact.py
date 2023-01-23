import logger as log

def ExportingSortedData(data):
    for i in log.SortingList(data):
        print(' '.join(i))
    return data

def ExportingChoosenPitchs(data):
    for i in log.ChoiseOfPitches(data):
        print(' '.join(i))
    return data











