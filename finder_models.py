from mongoengine import *

connect('db_info')

class Article(Document):
    # text = IntField()
    # url = IntField()
    text = StringField(max_lenght=120, unique=True)
    url = StringField(max_lenght=200, unique=True)
    # date = DataField()

    def __str__(self):
        return self.text



# class Tasks(Document):
#     user_chat_id = StringField(max_lenght=200)
#     flag_done = BoleanField(default=False)
#     query = StringField()

#     def __str__(self):
#         return self.user_chat_id