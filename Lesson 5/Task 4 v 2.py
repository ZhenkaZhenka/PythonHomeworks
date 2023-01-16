# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E

# Отличине от Task 4 v 1.py только в методе сжатие, здесь я использую словарь
# Подробное описание в Task 4 v 1.py

text = input('Input text to compress: ')
compressedText = ''

dict = {}
def CompressText(text):
    compressedText = ''
    for i in range(len(text)): # Проходим по каждому символу в тексте и создаем уникальные ключи для словаря
        dict[text[i]] = 0 # Каждый ключ делает целочисленным и равных 0
    for i in range(len(text)): # Снова проходим текст для подсчета количества каждого элемента
        if text[i] in dict.keys(): # Если символ из текста-ключ, то значение в словаре для этого ключа +1
            dict[text[i]] += 1
    for key in dict: # Создаем текст из пар значение+ключ
        compressedText += str(dict[key]) + key
    dict.clear() # чистим словарь, чтобы не создавать несколько
    return compressedText

def DecompressText(text):
    decompressedText = ''
    for i in range(1, len(text), 2):
        dict[text[i]] = text[i - 1]
    for key in dict.keys():
        temp = int(dict[key])
        while temp>0:
            decompressedText += str(key)
            temp -= 1
    dict.clear()
    return decompressedText


# Тут я два раза сжимаю и раскрываю введеный текст
compressedText = CompressText(text)
decompressedText = DecompressText(compressedText)
compressedText2 = CompressText(decompressedText)
decompressedText2 = DecompressText(compressedText2)

print('Compressed input text is:', compressedText)
print('Decompressed text after compression is:', decompressedText)
print('Compressed decompressed text is:', compressedText2)
print('Decompressed compressed decopressed text is:', decompressedText2)
