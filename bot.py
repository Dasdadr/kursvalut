from config import TOKEN
import telebot

from telebot.types import (

    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton

)

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")




bot.infinity_polling()

