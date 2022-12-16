# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Input N: '))
k = int(input('How many elements you want to multiply? '))

list = [i for i in range(-n, n+1)]

result = 1

with open('Task4.txt', 'w') as text:
    while k != 0:
        set_ok = False #просто поупражняться как работает, лучше ли это выносить в отдельный метод?
        while(set_ok != True):
            try:
                print('Input index of number:')
                temp = input()
                if temp.isdigit():
                    set_ok = True
                else: 
                    print('Input a number, not a string')
            except: # Этот блок не работает почему-то, поэтому я добавил else в предыдущие две строки
                print('Input a number, not a string')
        text.write(temp+"\n")
        k -= 1

with open('Task4.txt', 'r') as text:
    for l in text:
        result *= list[int(l)]

print('Array from -N until N:')
print(list)
print("Result of the multiply numbers from array with input indexes is " + str(result))
