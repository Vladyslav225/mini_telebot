import telebot
from telebot import types
from configure import config
# from GoW_checking_words import check_user_word
from GoW_checking_words import last_letter_bot_word
from GoW_checking_words import bot_words


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
     n = types.ReplyKeyboardMarkup()
     n.add(types.KeyboardButton('Бот'), types.KeyboardButton('Игрок'))
     
     n = bot.send_message(message.chat.id, 'Я или Ты?', reply_markup=n)
     bot.register_next_step_handler(n, choose_first_move)

# Решение определения, кто сделает первый ход (Игрок или Бот)
def choose_first_move(message):
     if message.text == 'Бот':
          bot_first_move = bot.send_message(message.chat.id, 'Хорошо, я начну первым :)')
          bot.register_next_step_handler(bot_first_move, bot_word(message))

     elif message.text == 'Игрок':
          gamer_first_move = bot.send_message(message.chat.id, 'Начинай :)')
          bot.register_next_step_handler(gamer_first_move, gamer_word(message))

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


def bot_word(message):
     bot.send_message(message.chat.id, 'Подожди, пожалуйста...')
     
     bot.send_message(message.chat.id, bot_words())
     bot.send_message(message.chat.id, f'Говори слово на букву: {last_letter_bot_word()}')

     bot.register_next_step_handler(message, gamer_word)


def gamer_word(message):
     bot.send_message(message.chat.id, f'{message.text}')



bot.polling(none_stop=True, timeout=0)


