import os
import random
import telebot
from telebot.types import Message
from decouple import config

TOKEN = config('TOKEN')

bot = telebot.TeleBot(TOKEN)

smiles = [
    '😜',
    '😍',
    '😁',
    '😁',
    '😊',
    '❤️',
]

# bot.send_message(391586450, 'hi from script')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    if message.from_user.id == 391586450:
        bot.reply_to(message, 'Good Morning')
    else:
        bot.reply_to(message, 'Good BYE')


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice(smiles))


bot.polling()
