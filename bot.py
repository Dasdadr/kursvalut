from config import TOKEN
import schedule, time
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pars

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
    print(message)
    data_text = "Здраствуйте, что бы узнать текущий курс валют нажмите на кнопку ниже👇👇👇"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    kurs = InlineKeyboardButton("Текущий курс", callback_data="tkurs")
    markup.add(kurs)
    # notf = InlineKeyboardButton("Отправлять мне уведомление", callback_data="notification")
    # markup.add(notf)
    feedback_btn = InlineKeyboardButton("Оставить отзыв", callback_data="feedback")
    markup.add(feedback_btn)
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == "tkurs")
def kursvalut(call):
     message = call.message
     print(message)
     base_url = 'https://www.akchabar.kg/ru/exchange-rates/'
     r = requests.get(base_url)
     soup = BeautifulSoup(r.text, 'html.parser')

     msgs = soup.find('div', {'id': 'rates'})
     msgs = msgs.text

     bot.send_message(message.chat.id, text=msgs, )







@bot.callback_query_handler(func=lambda call: call.data == "feedback" )
def answer_of_feedback_callback(call):
    message = call.message
    print(message)
    text = "Напишите что вы об этом думаете "
    bot.send_message(message.chat.id, text, reply_markup=None)
    bot.register_next_step_handler(message=message, callback=get_feedback)


def get_feedback(message):

    from datetime import datetime
    text_of_message = message.text
    print(text_of_message)
    username = message.from_user.username
    print(username)
    message_date_time = message.date
    message_conv_time = datetime.fromtimestamp(message_date_time).strftime("%d-%m-%Y %H:%M:%S")
    print(message_conv_time)
    with open("feedbacks.txt", "a", encoding="utf-8") as file:
        full_text = f"""
        Время создания: {message_conv_time}
        Логин пользователя: {username}
        Текст отзыва: {text_of_message}
    """
        file.write(full_text)










bot.polling()




