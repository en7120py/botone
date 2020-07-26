# /main.py file
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import os
from telebot import types

token = os.getenv('API_BOT_TOKEN')
bot = telebot.TeleBot(token)

known_users = []
user_steps = {}
commands = {
    'start': 'Start using this bot',
    'help': 'Useful information about this bot',
    'contacts': 'Contacts'
}


def send_action(action):
    """Send 'action' while processing  function command."""
    def decorator(func):
        @wraps(func)
        def command_func(message, *args, **kwargs):
            bot.send_chat_action(chat_id=message.chat.id, action=action)
            return func(message, *args, **kwargs)

        return command_func
        return decorator


@bot.message_handler(commands=['start'])
def command_start_handler(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add('button_geo')
    bot.send_message(cid, 'Hello! Choose commands, please', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
