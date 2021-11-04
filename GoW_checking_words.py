# from GoW_word_search_module import get_word
import random

bot_library_words = ['яблоко', 'арбуз', 'помидор']

used_user_words = []
used_bot_words = []

user_word = ''
bot_word = ''
# word = ''


def check_user_word():

     if user_word == used_user_words:
          return('Ты уже говорил это слово')

     elif user_word == used_bot_words:
          return('Я уже говорил это слово')

     elif user_word == "" or user_word == " ":
          return('Запрещено отправлять пустую строку')

     elif len(user_word) <= 2:
          return ('В твоем слове недостаточно букв')

     used_user_words.append(user_word)
     bot_word = bot_library_words(user_word[-1])
     return bot_word

check_user_word()




def input_bot_words():
     bot_word = random.choice(bot_library_words)

     last_index = bot_word[-1]
     send_word_last_letter = (f'{bot_word} .Говори слово на букву: {last_index}')
     
     return send_word_last_letter

# def last_letter_bot_word():
#      last_letter = word[-1]

#      return (f'Говори слово на букву: {last_letter}')


# send_last_letterz = 
input_bot_words()
# print(bot_word, n)

# last_letter_bot_word()
