from telebot import TeleBot
from telebot import types

import json

import configure

EQUIPMENT_CATEGORIES = 'kiy_v_json/equipment_categories.json'

bot = TeleBot(configure.config['token'])

@bot.message_handler(commands=['get_categories_product'])
def get_product(message):
    with open(EQUIPMENT_CATEGORIES) as file:
        categories = json.load(file)
        cat = categories[0]['Image category']
        cat1 = categories[1]['Image category']
        cat2 = categories[2]['Image category']
        cat3 = categories[3]['Image category']
        cat4 = categories[4]['Image category']
        cat5 = categories[5]['Image category']
        cat6 = categories[6]['Image category']
        cat7 = categories[7]['Image category']
        cat8 = categories[8]['Image category']
        cat9 = categories[9]['Image category']
#     categ = value['name category']#'\n'{value['URL category']}\n{value['Image category']}
    bot.send_message(message.chat.id, cat)
    bot.send_message(message.chat.id, cat1)
    bot.send_message(message.chat.id, cat2)
    bot.send_message(message.chat.id, cat3)
    bot.send_message(message.chat.id, cat4)
    bot.send_message(message.chat.id, cat5)
    bot.send_message(message.chat.id, cat6)
    bot.send_message(message.chat.id, cat7)
    bot.send_message(message.chat.id, cat8)
    bot.send_message(message.chat.id, cat9)

#     print(123)
        
    # markup_inline = types.InlineKeyboardMarkup()
    # equipment_categories = types.InlineKeyboardButton(text = 'Оборудование', callback_data = 'equipment')

# @bot.message_handler(content_types=['text'])
# def test(message):
#     if message.text == 'hi':
#         bot.send_message(message.chat.id, 'hi, boy')


bot.infinity_polling()

