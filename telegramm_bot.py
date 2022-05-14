import telebot
#285136154 chat id
bot = telebot.TeleBot("5205956746:AAEJEmUXPYixp_oXY-WPa4106Tk0UNWwCxw")


def sendMessage(text):
    bot.send_message(285136154, text)
