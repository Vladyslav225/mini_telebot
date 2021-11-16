from mongoengine import *
connect('db_words_bot_and_users')

class BotWords(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)

a = BotWords(email='asd@', first_name='qwe')
a.save()