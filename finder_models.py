from mongoengine import *

connect('db_info')

class DataParsing(Document):

    print('DataParsing')
    
    text = StringField(max_lenght=120)
    url = StringField(max_lenght=200)

    def __str__(self):
        return self.text



class DataUser(Document):

    print('DataUser')

    user_chat_id = IntField()
    query = StringField()

    def __str__(self):
        return self.user_chat_id
