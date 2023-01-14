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

for i in range(len(text)):
    dict[text[i]] = 0

for i in range(len(text)):
    if text[i] in dict.keys():
        dict[text[i]] += 1

print(dict)

for key in dict:
    compressedText += str(dict[key]) + key

print(compressedText)
