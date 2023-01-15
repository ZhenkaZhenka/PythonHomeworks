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


text = input('Input text to compress: ')
compressedText = ''

dict = {}
def CompressText(text):
    compressedText = ''
    for i in range(len(text)):
        dict[text[i]] = 0
    for i in range(len(text)):
        if text[i] in dict.keys():
            dict[text[i]] += 1
    for key in dict:
        compressedText += str(dict[key]) + key
    dict.clear()
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

compressedText = CompressText(text)
decompressedText = DecompressText(compressedText)
compressedText2 = CompressText(decompressedText)
decompressedText2 = DecompressText(compressedText2)

print('Compressed input text is:', compressedText)
print('Decompressed text after compression is:', decompressedText)
print('Compressed decompressed text is:', compressedText2)
print('Decompressed compressed decopressed text is:', decompressedText2)
