# /main.py file
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# dependencies
import telebot
import os
from telebot import types

token = os.getenv('API_BOT_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def command_start_handler(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add('button_geo')
    bot.send_message(cid, 'Hello! Choose commands, please', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
