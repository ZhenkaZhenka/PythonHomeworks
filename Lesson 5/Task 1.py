# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = input('Input any text to work with it: ')

list = text.split(' ')

for i in list:
    for j in range(len(i) - 2):
        if i[j] == 'а':
            if i[j + 1] == 'б':
                if i[j + 2] == 'в':
                    list.remove(i)

newText = ' '.join(list)

print(newText)