import telebot
from telebot import types
from random import randint

TOKEN = 'Input your token'

bot = telebot.TeleBot(TOKEN)

amount_of_candies = 0
max_amount_of_candies = 28
player_1_name = ''
player_2_name = ''
type = 2

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "/buttons")##Реакция бота на команду /start


@bot.message_handler(commands = ["buttons"])
def button1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)##
    but1 = types.KeyboardButton("Rules")
    but2 = types.KeyboardButton("PlayerVsPlayer")
    but3 = types.KeyboardButton("PlayerVsBot")
    but4 = types.KeyboardButton("PlayerVsCleverBot")
    but5 = types.KeyboardButton("Stop")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    bot.send_message(message.chat.id, "Выберите ниже", reply_markup = markup)

def button2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)##
    but1 = types.KeyboardButton("Я сам хочу начать")
    but2 = types.KeyboardButton("Пусть Бот ходит первый")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выберите ниже", reply_markup = markup)

@bot.message_handler(content_types = "text")
def controller(message):
    global type
    if message.text == "Rules":
        rules(message)
    elif message.text == "PlayerVsPlayer":
        bot.send_message(message.chat.id, "Вы выбрали режим Игрок против Игрока")
        playervsplayerstart(message)
    elif message.text == "PlayerVsBot":
        bot.send_message(message.chat.id, "Вы выбрали режим Игрок против Бота")
        type = 2
        playervsbotstart(message)
    elif message.text == "PlayerVsCleverBot":
        bot.send_message(message.chat.id, "Вы выбрали режим Игрок против умного Бота")
        type = 1
        playervsbotstart(message)
    else: return

def rules(message):
    bot.send_message(message.chat.id, "Условие задачи: На столе лежит 221 конфета. "
                                      "Играют два игрока делая ход друг после друга. "
                                        "За один ход можно забрать не более чем 28 конфет. "
                                      "Побеждает тот кто забирает последнюю конфету")
    button1(message)
def playervsplayerstart(message):
    global amount_of_candies
    amount_of_candies = 221
    bot.send_message(message.chat.id, 'Игрок 1, введите свое имя')
    bot.register_next_step_handler(message, player1name)


def player1name(message):
    global player_1_name
    player_1_name = message.text
    bot.send_message(message.chat.id, 'Игрок 2, введите свое имя')
    bot.register_next_step_handler(message, player2name)


def player2name(message):
    global player_2_name
    player_2_name = message.text
    bot.send_message(message.chat.id, 'Пожалуй начнем')
    playervsplayer1player(message)


def playervsplayer1player(message):
    global amount_of_candies
    global max_amount_of_candies
    bot.send_message(message.chat.id, str(amount_of_candies) + ' candies last')
    bot.send_message(message.chat.id,
                     str(player_1_name) + ', now is your turn, input of candies but no more ' + str(
                         max_amount_of_candies))
    bot.register_next_step_handler(message, turn1player)


def turn1player(message):
    global max_amount_of_candies
    global player_amount
    try:
        player_amount = int(message.text)
        if (player_amount <= max_amount_of_candies and player_amount >= 0):
            count1player(message)
        else:
            e
    except Exception as e:
        bot.send_message(message.chat.id,
                         'Input integer amount of candies from 0 to ' + str(max_amount_of_candies))
        bot.register_next_step_handler(message, turn1player)


def count1player(message):
    global amount_of_candies
    global max_amount_of_candies
    step = player_amount
    amount_of_candies -= step
    if amount_of_candies < max_amount_of_candies:
        max_amount_of_candies = amount_of_candies
    if checkwinner():
        bot.send_message(message.chat.id, str(player_1_name) + ' you are winner')
        return
    playervsplayer2player(message)


def playervsplayer2player(message):
    global amount_of_candies
    global max_amount_of_candies
    bot.send_message(message.chat.id, str(amount_of_candies) + ' candies last')
    bot.send_message(message.chat.id,
                     str(player_2_name) + ', now is your turn, input of candies but no more ' + str(
                         max_amount_of_candies))
    bot.register_next_step_handler(message, turn2player)


def countplayer2(message):
    global amount_of_candies
    global max_amount_of_candies
    step = player_amount
    amount_of_candies -= step
    if amount_of_candies < max_amount_of_candies:
        max_amount_of_candies = amount_of_candies
    if checkwinner():
        bot.send_message(message.chat.id, str(player_2_name) + ' you are winner')
        button1(message)
        return
    playervsplayer1player(message)

def checkwinner():
    global amount_of_candies
    if amount_of_candies <= 0:
        return True

def turn2player(message):
    global max_amount_of_candies
    global player_amount
    try:
        player_amount = int(message.text)
        if (player_amount <= max_amount_of_candies and player_amount >= 0):
            count1player(message)
        else:
            e
    except Exception as e:
        bot.send_message(message.chat.id,
                         'Input integer amount of candies from 0 to ' + str(max_amount_of_candies))
        bot.register_next_step_handler(message, turn1player)

##Здесь начинаются методы игры против бота
def playervsbotstart(message):
    global amount_of_candies
    global max_amount_of_candies
    amount_of_candies = 221
    max_amount_of_candies = 28
    bot.send_message(message.chat.id, 'Игрок, введите свое имя')
    bot.register_next_step_handler(message, playername)

def playername(message):
    global player_1_name
    player_1_name = message.text
    bot.send_message(message.chat.id, 'OK, давай начнем. Кто будет ходить первым?')
    button2(message)
    bot.register_next_step_handler(message, choiseturn)

def choiseturn(message):
    if message.text == 'Я сам хочу начать':
        playervsbotplayer(message)
    elif message.text == 'Пусть Бот ходит первый':
        playervsbotbot(message)
    else:
        bot.send_message(message.chat.id, 'Так не пойдет, тебе нужно выбрать из двух')
        button2(message)

def playervsbotplayer(message):
    global amount_of_candies
    global max_amount_of_candies
    bot.send_message(message.chat.id, str(amount_of_candies) + ' candies last')
    bot.send_message(message.chat.id,
                     str(player_1_name) + ', now is your turn, input of candies but no more ' + str(
                         max_amount_of_candies))
    bot.register_next_step_handler(message, turnplayer)

def countplayer(message):
    global amount_of_candies
    global max_amount_of_candies
    step = player_amount
    amount_of_candies -= step
    if amount_of_candies < max_amount_of_candies:
        max_amount_of_candies = amount_of_candies
    if checkwinner():
        bot.send_message(message.chat.id, str(player_1_name) + ' you are winner')
        button1(message)
        return
    playervsbotbot(message)

def turnplayer(message):
    global max_amount_of_candies
    global player_amount
    try:
        player_amount = int(message.text)
        if (player_amount <= max_amount_of_candies and player_amount >= 0):
            count1player(message)
        else:
            e
    except Exception as e:
        bot.send_message(message.chat.id,
                         'Input integer amount of candies from 0 to ' + str(max_amount_of_candies))
        bot.register_next_step_handler(message, turn1player)

def playervsbotbot(message):
    global amount_of_candies
    global max_amount_of_candies
    bot.send_message(message.chat.id, str(amount_of_candies) + ' candies last')
    turnbot(message)

def turnbot(message):
    global player_amount
    global type
    if type == 2:
        player_amount = randint(0, max_amount_of_candies)
    else:
        player_amount = amount_of_candies % (max_amount_of_candies + 1)
    bot.send_message(message.chat.id, f"Bot took {player_amount} candies")
    countbot(message)

def countbot(message):
    global amount_of_candies
    global max_amount_of_candies
    step = player_amount
    amount_of_candies -= step
    if amount_of_candies < max_amount_of_candies:
        max_amount_of_candies = amount_of_candies
    if checkwinner():
        bot.send_message(message.chat.id, "Bot won, you are loser")
        button1(message)
        return
    playervsbotplayer(message)


bot.infinity_polling()

