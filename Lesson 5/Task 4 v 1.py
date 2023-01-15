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

# Работает только тогда, когда символов подряд не больше 9.

text = input('Input word to compress: ')
i = 0

def CompressText(text):  # Метод сжатия введенного текста
    compressedText = ''
    i = 0
    while i < len(text):
        counter = 0
        while text[i] == text[i + counter]: # Выполняем пока символы в ряду одинаковые подряд
            counter += 1 # Считаем количество подряд идущих элементов и используем его как шаг для сравнения
            if (i + counter) == len(text): break # в последней иттерации подсчета индекс [i + counter] выходит за пределы размера текста
        compressedText += str(counter) + text[i] # Добавляю в сжатый текст количество подряд идущийх элементов и элемент
        i += counter # меняю i для пропуска подряд идущих элементов
    return compressedText

def DecompressText(text):
    dict = {} 
    decompressedText = ''
    for i in range(1, len(text), 2): # Начинаю со второго элемента в качестве символа, который будет повторяться
        dict[text[i]] = text[i - 1] # [i - 1] - количество повторений
    for key in dict.keys():
        temp = int(dict[key]) # Количество повторений из 35 строки
        while temp > 0: 
            decompressedText += str(key) # Вписываем значение ключа в текст
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