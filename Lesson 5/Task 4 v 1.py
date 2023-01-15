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

text = input('Input word to compress: ')
i = 0

def CompressText(text):
    compressedText = ''
    i = 0
    while i < len(text):
        counter = 0
        while text[i] == text[i + counter]:
            counter += 1
            if (i + counter) == len(text): break
        compressedText += str(counter) + text[i]
        i += counter
    return compressedText



def DecompressText(text):
    dict = {}
    decompressedText = ''
    for i in range(1, len(text), 2):
        dict[text[i]] = text[i - 1]
    for key in dict.keys():
        temp = int(dict[key])
        while temp>0:
            decompressedText += str(key)
            temp -= 1
    return decompressedText

compressedText = CompressText(text)
decompressedText = DecompressText(compressedText)
compressedText2 = CompressText(decompressedText)
decompressedText2 = DecompressText(compressedText2)

print('Compressed input text is:', compressedText)
print('Decompressed text after compression is:', decompressedText)
print('Compressed decompressed text is:', compressedText2)
print('Decompressed compressed decopressed text is:', decompressedText2)