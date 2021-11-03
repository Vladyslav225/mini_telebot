bot_library_words = ['яблоко', 'арбуз', 'помидор']
my_used_words = []

def get_word(first_letter):
     for bot_word in bot_library_words:
          if bot_word[0] == first_letter and (bot_word in my_used_words) == False:
               my_used_words.append(bot_word)
               return bot_word
