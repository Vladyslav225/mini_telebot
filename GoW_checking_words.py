# from GoW_word_search_module import get_word
bot_library_words = ['яблоко', 'арбуз', 'помидор']

used_user_words = []
used_bot_words = []

# bot_word = ''



# def check_user_word(user_word, bot_word):

#      if user_word == used_user_words:
#           return('Ты уже говорил это слово')

#      elif user_word == used_bot_words:
#           return('Я уже говорил это слово')

#      elif user_word == "" or user_word == " ":
#           return('Запрещено отправлять пустую строку')

#      elif bot_word == None:
#           return('Я не знаю этого слова')

#      elif len(user_word) <= 2:
#           return ('Втвоем слове недостаточно букв')

     
#      used_user_words.append(user_word)
#      bot_word = bot_library_words(user_word[-1])
#      return bot_word

# check_user_word()




def bot_words():
     bot_word = bot_library_words[1]
     return bot_word

def last_letter_bot_word():
     letter = n[-1]

     return letter
bot_words()
n = bot_words()
# print(n)
# print(last_letter_bot_word())
