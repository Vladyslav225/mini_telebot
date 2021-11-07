# from GoW_word_search_module import get_word
import random

bot_library_words = ['яблоко', 'арбуз', 'помидор']

used_user_words = []
used_bot_words = []

user_word = ''
bot_word = ''


def check_user_word():
     print(123)
     if user_word == used_user_words:
          return('Ты уже говорил это слово')

     elif user_word == used_bot_words:
          return('Я уже говорил это слово')

     elif user_word == "" or user_word == " ":
          return('Запрещено отправлять пустую строку')

     elif len(user_word) <= 2:
          return ('В твоем слове недостаточно букв')

     used_user_words.append(user_word)
     word = user_word[-1]
     return word

user_word = check_user_word()




def input_bot_words():
     global bot_word
     bot_word = random.choice(bot_library_words)
     
     return bot_word

def last_letter_bot_word():
     last_letter = bot_word[-1]

     return (f'Говори слово на букву: {last_letter}')


# send_last_letterz = 
send_word = input_bot_words()
# print(b)

send_last_index = last_letter_bot_word()
# print(n)
