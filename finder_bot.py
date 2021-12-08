from telebot import TeleBot
import types

import time
import json

from configure import finder
from finder_models import Article, Tasks

bot = TeleBot(finder['token'])

@bot.message_handler(content_types = ['text'])
def get_text(message):
    print(123)


bot.polling(none_stop = True, interval = 0)