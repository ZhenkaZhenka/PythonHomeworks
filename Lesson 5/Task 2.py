# Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, 
#            чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

from random import randint

def ChoiseOfTheGamesType(condition, amountOfCandies, maxAmountOfCandies):
    while condition:
        try:
            type = input('Hello, choise the type of game( 1: Player vs Player, 2: Player vs Bot, 3: Player vs Clever bot(Impossible to win)): ').lower()
            match(type):
                case '1': 
                    PlayerVsPlayer(amountOfCandies, maxAmountOfCandies)
                    condition = GetNewGame('Do you want to play again? Write "No", if you dont want: ')
                case '2': 
                    PlayerVsBot(amountOfCandies, maxAmountOfCandies, int(type))
                    condition = GetNewGame('Do you want to play again? Write "No", if you dont want: ')
                case '3': 
                    PlayerVsBot(amountOfCandies, maxAmountOfCandies, int(type))
                    condition = GetNewGame('Do you want to play again? Write "No", if you dont want: ')
                case _: e
        except Exception as e:
            print('Game doesnt have this type')

def TurnPlayer(maxAmountOfCandies):
    while True:
        try:
            playerAmount = int(input())
            if (playerAmount <= maxAmountOfCandies and playerAmount >= 0):
                return playerAmount
            else: e
        except Exception as e:
            print('Input amountOfCandies of candies from 0 to', maxAmountOfCandies)

def GetNewGame(message):
    print(message)
    while True:
        try:
            word = input()
            if word.lower() == 'no':
                print('Ok, have a good day')
                return False
            elif word.lower() == 'yes':
                print('Perfect, lets start!')
                return True
            else: e
        except Exception as e:
            print('Pls, fill in "Yes" or "No"')

def CheckWinner(amountOfCandies):
    if amountOfCandies == 0:
        return True

def TurnBot(amountOfCandies, type, maxAmountOfCandies):
    if type == 2:
        return randint(0, maxAmountOfCandies)
    else:
        return amountOfCandies % (maxAmountOfCandies + 1)

def PlayerVsPlayer(amountOfCandies, maxAmountOfCandies):
    player1Name = input('Player 1, pls, input name that you want to use in game: ')
    player2Name = input('Player 2, pls, input name that you want to use in game: ')
    while (amountOfCandies > 0):
        print(player1Name, ', now is your turn, input amountOfCandies of candies but no more ', maxAmountOfCandies)
        step = TurnPlayer(maxAmountOfCandies)
        amountOfCandies -= step
        if amountOfCandies < maxAmountOfCandies:
            maxAmountOfCandies = amountOfCandies
        if CheckWinner(amountOfCandies):
            print(player1Name + 'you are winner, congradulation')
            break
        print(amountOfCandies, ' candies last')
        print(player2Name, ', now is your turn, input amountOfCandies of candies but no more ', maxAmountOfCandies)
        step = TurnPlayer(maxAmountOfCandies)
        amountOfCandies -= step
        if amountOfCandies < maxAmountOfCandies:
            maxAmountOfCandies = amountOfCandies
        if CheckWinner(amountOfCandies):
            print(player2Name, 'you are winner, congradulation')
            break
        print(amountOfCandies, ' candies last')
    return

def PlayerVsBot(amountOfCandies, maxAmountOfCandies, type):
    player1Name = input('Player 1, pls, input name that you want to use in game: ')
    while (amountOfCandies > 0):
        print(player1Name, ', now is your turn, input amountOfCandies of candies but no more ', maxAmountOfCandies)
        step = TurnPlayer(maxAmountOfCandies)
        amountOfCandies -= step
        if amountOfCandies < maxAmountOfCandies:
            maxAmountOfCandies = amountOfCandies
        if CheckWinner(amountOfCandies):
            print(player1Name + 'you are winner, congradulation')
            break
        print(amountOfCandies, ' candies last')
        print('Bots turn, type of game is', type)
        step = TurnBot(amountOfCandies, type, maxAmountOfCandies)
        print('Bot took', step, 'candies')
        amountOfCandies -= step
        if amountOfCandies < maxAmountOfCandies:
            maxAmountOfCandies = amountOfCandies
        if CheckWinner(amountOfCandies):
            print('Bot has won, be cleverer next time')
            break
        print(amountOfCandies, ' candies last')
    return 

def Game():
    condition = GetNewGame('Do you wanna play? Input "Yes" or "No":')
    if condition:
        amountOfCandies = int(input('Input an amount of the candies: '))
        maxAmountOfCandies = int(input('Input a max amount of candies per step: '))
        ChoiseOfTheGamesType(condition, amountOfCandies, maxAmountOfCandies)
    else:
        return

Game()       
        
    

