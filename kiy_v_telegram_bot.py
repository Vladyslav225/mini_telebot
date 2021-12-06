from telebot import TeleBot
from telebot import types
from bs4 import BeautifulSoup
import requests
import json

import configure

EQUIPMENT_CATEGORIES = 'kiy_v_json/equipment_categories.json'
EQUIPMENT_PAGE_HTML = 'kiy_v_html/equipment_page.html'

bot = TeleBot(configure.config['token'])

@bot.message_handler(commands=['start'])
def get_product(message):
    bot.send_message(message.chat.id, 'Hi, input comman "/start" ')

@bot.message_handler(commands=['/categories'])
def info(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

    markup_reply.add(types.KeyboardButton('Печі і пароконвектомати'))
    
    bot.send_message(message.chat.id, '123', reply_markup=markup_reply)
    










bot.polling()

