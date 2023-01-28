import telebot
from telebot import types

TOKEN = 'Здесь место для вашего токенай'

bot = telebot.TeleBot(TOKEN)

amount_of_candies = 0
max_amount_of_candies = 28
player_1_name = ''
player_2_name = ''

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "/button")##Реакция бота на команду /start


@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)##
    but1 = types.KeyboardButton("PlayerVsPlayer")
    but2 = types.KeyboardButton("PlayerVsBot")
    but3 = types.KeyboardButton("PlayerVsCleverBot")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    bot.send_message(message.chat.id, "Выберите ниже", reply_markup = markup)

@bot.message_handler(content_types = "text")
def controller(message):
    if message.text == "PlayerVsPlayer":
        bot.send_message(message.chat.id, "Вы выбрали режим Игрок против Игрока")
        playervsplayerstart(message)
    elif message.text == "PlayerVsBot":
        bot.register_next_step_handler(message, "Pidor python")
    elif message.text == "PlayerVsCleverBot":
        bot.register_next_step_handler(message, 'Pidorpython2')
    else: return

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
                     str(player_1_name) + ', now is your turn, input amountOfCandies of candies but no more ' + str(
                         max_amount_of_candies))
    bot.register_next_step_handler(message, turn1player)


def turn1player(message):
    global max_amount_of_candies
    global player_amount

    player_amount = int(message.text)
    if (player_amount <= max_amount_of_candies and player_amount >= 0):
        count1player(message)
    else:
        bot.send_message(message.chat.id,
                         'Input amount of candies of candies from 0 to' + str(max_amount_of_candies))
        playervsplayer1player(message)


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
                     str(player_2_name) + ', now is your turn, input amountOfCandies of candies but no more ' + str(
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
        button()
        return
    playervsplayer1player(message)

def checkwinner():
    global amount_of_candies
    if amount_of_candies <= 0:
        return True

def turn2player(message):
    global max_amount_of_candies
    global player_amount
    player_amount = int(message.text)
    if (player_amount <= max_amount_of_candies and player_amount >= 0):
        countplayer2(message)
    else:
        bot.send_message(message.chat.id,
                         'Input amount of candies of candies from 0 to' + str(max_amount_of_candies))
        playervsplayer2player(message)

bot.infinity_polling()