from telebot import TeleBot
from telebot import types

from configure import finder
from finder_models import DataParsing, DataUser
from finder_connector import user_response_save_db

bot = TeleBot(finder['token'])

@bot.message_handler(commands = ['start'])
def get_text(message):

    print('get_text')
    
    bot.send_message(message.chat.id, 'Hi, finder! What do you want to find?')

@bot.message_handler(content_types = ['text'])
def get_information(message):

    print('get_information')

    id_user = message.from_user.id
    text_search = message.text.replace('/text', '')

    if not text_search:
        bot.send_message(id_user, 'OMG !')

        return

    bot.send_message(message.chat.id, 'Wait please ...')

    user_response_save_db(id_user, text_search)

    for data in DataParsing.objects:
        print(data.url)
        bot.send_message(message.chat.id, data.url)


bot.polling(none_stop = True, interval = 0)