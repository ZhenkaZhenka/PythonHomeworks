# Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту
# (как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), 
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу
# ( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)


# Печать листа
def PrintPitch(list):
    print(list[0], list[1],  list[2])
    print(list[3], list[4],  list[5])
    print(list[6], list[7],  list[8])
    return

# Установка символа в лист
def PutSign(list, point, char): 
    list[point-1] = char
    return list

# Не придумал ничего лучше, да и хотелось сделать до семинара
# Сравнение выйгрышных комбинаций
def CheckWin(list):  
    if list[0] == list[1] == list[2]: return True
    if list[3] == list[4] == list[5]: return True
    if list[6] == list[7] == list[8]: return True
    if list[0] == list[3] == list[6]: return True
    if list[1] == list[4] == list[7]: return True
    if list[2] == list[5] == list[8]: return True
    if list[0] == list[4] == list[8]: return True
    if list[2] == list[4] == list[6]: return True
    return False


# Дается выбор для игрка каким символом играть, но только "X" или "O", если игрок 1 выбирает любой символ отличный от "X", то он получает "O"
def ChoiseOfSigns(player1name, player2name, playerSign):
    if playerSign == 'X'.lower() or playerSign == 'Х'.lower(): return {player1name: 'X', player2name: 'O'}
    else: return {player1name: 'O', player2name: 'X'}

# Проверка есть ли введеная позиция с на поле
def CheckNumberOfPoint(list):
    while True:
        try:
            point = int(input('Input number 1-9: '))
            if point < 1 or point > 9:
                return e
            else: return point
        except Exception as e:
            print('Pitch doesnt have this point, plz, choise another point')

# Проверка занято ли поле
def CheckEmptyPoint(list):
    while True:
        try:
            point = CheckNumberOfPoint(list)
            if not str(list[point-1]).isdigit():
                return e
            else: return point
        except Exception as e:
            print('This point has been occupied, choise another point')

# Сама игра
def Game(list):
    player1name = input('Player 1, fill in name that you want to use in game: ') # Ввод имен игроков
    player2name = input('Player 2, fill in name that you want to use in game: ')
    print(player1name, 'choise the sign "X" or "O"') # Выбор символа игрока 1
    playerSign = input() # ввод символа
    dict = ChoiseOfSigns(player1name, player2name, playerSign) # Использую словарь для определения символа игрока, удобно
    counter = len(list) # Максимальное количество ходов, определяемое размером поля
    while True:
        print(player1name, 'choise the point on the pitch where you want to put your sign:')
        point = CheckEmptyPoint(list)
        PrintPitch(PutSign(list, point, dict[player1name]))
        if CheckWin(list):
            print(player1name, 'you are won, congradulation!')
            return
        counter -= 1
        if counter == 0: break
        print(player2name, 'choise the point on the pitch where you want to put your sign:')
        point = CheckEmptyPoint(list)
        PrintPitch(PutSign(list, point, dict[player2name]))
        if CheckWin(list):
            print(player2name, 'you are won, congradulation!')
            return
        counter -= 1
        if counter == 0: break
    if not CheckWin(list):
        print('Nobody won, game has to have winner!')
    return
    
def WannaPlay():
    play = input()
    if play == 'Yes'.lower() or play == 'Yep'.lower() or play == 'Yeah'.lower():
        return True
    else:
        print('Ok, next time!')
        return False

def ActivationOfGame(list):
    print('Hello everyone, do you want to play? Fill in "Yes" or "No": ')
    stateOfGame = WannaPlay()
    while stateOfGame:
        list = [i for i in range(1,10)]
        Game(list)
        print('Do you wanna play again?')
        stateOfGame = WannaPlay()
    return

ActivationOfGame(list)

    


