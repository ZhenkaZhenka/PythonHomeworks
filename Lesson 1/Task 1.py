# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Input number of a day of week: '))

if number < 1 or number > 7:
    print('Number is not a day of week')
elif number > 5 and number < 8:
    print('This day is a weekend')
elif number > 0 and number < 6:
    print('This day is not a weekend')
