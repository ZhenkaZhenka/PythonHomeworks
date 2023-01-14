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
compressedText = ''
i = 0

while i < len(text):
    counter = 0
    while text[i] == text[i + counter]:
        counter += 1
        if (i + counter) == len(text): break
    compressedText += str(counter) + text[i]
    i += counter


print(compressedText)
