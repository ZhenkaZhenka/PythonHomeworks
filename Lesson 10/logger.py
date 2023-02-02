from datetime import datetime as dt

def LogExport(data, message):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} {} {} calculated equation {}\n'
                   .format(time, message.chat.first_name, message.chat.last_name, data))
    return data

def LogInput(data, message):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} {} {} input {}\n'
                   .format(time, message.chat.first_name, message.chat.last_name, data))
    return data