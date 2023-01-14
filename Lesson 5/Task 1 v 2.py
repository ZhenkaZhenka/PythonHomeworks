# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = input('Input text')

text = ' '.join(list(filter(lambda word: not 'абв' in word, text.split())))

print(text)