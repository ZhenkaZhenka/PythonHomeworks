import telebot
import logger as log
from telebot import types


TOKEN = 'Token'

bot = telebot.TeleBot(TOKEN)

sign_after_comma = 0

@bot.message_handler(commands = ["start"])
def typesbuttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Real numbers")
    but2 = types.KeyboardButton("Rational numbers")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Hello, this is simple calculator. "
                                      "Choose choose type of numbers below", reply_markup = markup)


@bot.message_handler(content_types=["text"])
def choisetype(message):
    text = message.text
    if text == "Real numbers":
        bot.send_message(message.chat.id, "Input equation via space")
        bot.register_next_step_handler(message, getresultreal)
    elif text == "Rational numbers":
        bot.send_message(message.chat.id, "Input equation via space")
        bot.register_next_step_handler(message, getresultrational)
    else:
        bot.send_message(message.chat.id, "Sorry, something went wrong")
        return
        # bot.register_next_step_handler(message, typesbuttons)


def getresultrational(message):
    equation = message.text.split()
    log.LogInput(message.text, message)
    a = float(equation[0])#getrationalorrealnumber(message, equation[0], type)
    b = float(equation[2])#getrationalorrealnumber(message, equation[2], type)
    match equation[1]:
        case '+':
            bot.send_message(message.chat.id, str(a + b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
        case '-':
            bot.send_message(message.chat.id, str(a - b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
        case '*':
            bot.send_message(message.chat.id, str(a * b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
        case '/':
            bot.send_message(message.chat.id, str(a / b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
        case _:
            bot.send_message(message.chat.id, "Sorry, something went wrong, try again3")
    bot.register_next_step_handler(message, choisetype)

def getresultreal(message):
    equation = message.text.split()
    log.LogInput(message.text, message)
    a = int(equation[0])
    b = int(equation[2])
    match equation[1]:
        case '+':
            bot.send_message(message.chat.id, str(a + b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
            bot.register_next_step_handler(message, choisetype)
        case '-':
            bot.send_message(message.chat.id, str(a - b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
            bot.register_next_step_handler(message, choisetype)
        case '*':
            bot.send_message(message.chat.id, str(a * b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
            bot.register_next_step_handler(message, choisetype)
        case '/':
            bot.send_message(message.chat.id, str(a / b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
            bot.register_next_step_handler(message, choisetype)
        case '//':
            bot.send_message(message.chat.id, str(a // b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
            bot.register_next_step_handler(message, choisetype)
        case '%':
            bot.send_message(message.chat.id, str(a % b))
            log.LogExport("{} {} {}".format(equation[0], equation[1], equation[2]), message)
            bot.register_next_step_handler(message, choisetype)
        case _:
            bot.send_message(message.chat.id, "Sorry, something went wrong, try again2")
            bot.register_next_step_handler(message, getresultreal)


bot.infinity_polling()

