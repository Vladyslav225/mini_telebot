import telebot
from telebot import types
from configure import config
from GoW_checking_words import check_user_word
from GoW_checking_words import last_letter_bot_word
from GoW_checking_words import input_bot_words
import time


bot = telebot.TeleBot(config['token'])

# Кнопка для отображения Правил игры
@bot.message_handler(commands= ['info_game'])
def get_info_game(message):
     markup_inline = types.InlineKeyboardMarkup()
     button_info = types.InlineKeyboardButton(text='Нажми меня :)', callback_data='info_game')

     markup_inline.add(button_info)
     bot.send_message(message.chat.id, 'Правила игры!',
          reply_markup=markup_inline
     )

# Подключение файла с Правилами игры
@bot.callback_query_handler(func = lambda call: True)
def answer_info(call):
     if call.data == 'info_game':
          bot.send_message(call.message.chat.id, 'Ты какашка :)')

# Определение, кто сделает первый ход (Игрок или Бот)
@bot.message_handler(commands= ['first_move'])
def who_first_move(message):
     markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
     markup_reply.add(types.KeyboardButton('Бот'), types.KeyboardButton('Игрок'))
     
     bot.send_message(message.chat.id, 'Я или Ты?', reply_markup=markup_reply)
     # bot.send_message(message.chat.id, '123')
     bot.register_next_step_handler_by_chat_id(message.chat.id, choose_first_move)

# Решение определения, кто сделает первый ход (Игрок или Бот)
def choose_first_move(message):
     if message.text == 'Бот':
          bot_move = bot.send_message(message.chat.id, 'Хорошо, я начну первым :)')
          # bot.register_next_step_handler(bot_first_move, start_game(message))
          bot.register_next_step_handler(bot_move, bot_word(message=bot_move))

     elif message.text == 'Игрок':
          gamer_first_move = bot.send_message(message.chat.id, 'Начинай :)')
          # bot.register_next_step_handler(gamer_first_move, start_game(message))
          bot.register_next_step_handler(gamer_first_move, gamer_word(message=gamer_first_move))


def bot_word(message):
     bot.send_message(message.chat.id, 'Подожди, пожалуйста...')
     time.sleep(5)

     bot.send_message(message.chat.id, input_bot_words())
     last_index = bot.send_message(message.chat.id, last_letter_bot_word())
     bot.register_next_step_handler(last_index, gamer_word)

def gamer_word(message):
     bot.send_message(message.chat.id, 'валяй')
     user_word = message.text
     user_word = bot.send_message(message.chat.id, check_user_word())
     bot.register_next_step_handler(user_word, bot_word(message=user_word))


# ----------------------------------------------------------------------------------


#Приветствие с Игроком
@bot.message_handler(content_types=['text'])
def welcome_user(message):
     bot.send_message(message.chat.id, f'Добро пожаловать в игру "Game of Words", {message.from_user.first_name} {message.from_user.last_name} (ID: {message.from_user.id})')


# Команда для вывода Правил игры
     bot.send_message(message.chat.id, 'Перед началом игры ознакомся с Правилами игры (/info_game)')
     bot.register_next_step_handler(message, first_move)


#Команда для определения, кто начнет игру
def first_move(message):
     bot.send_message(message.chat.id, 'Давай решим, кто сделает первый ход (/first_move)')



bot.infinity_polling(allowed_updates = None, 
     long_polling_timeout = 20
     )

