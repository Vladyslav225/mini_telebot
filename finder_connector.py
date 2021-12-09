from finder_models import DataParsing, DataUser

from finder_parser import parser


def user_response_save_db(id_user, text_search):

    print('user_response_save_db')

    DataUser(user_chat_id=id_user, query=text_search).save()

    for data in DataUser.objects:
        print(data.query)

def parsing_answer_save_db():

    print('parsing_answer_save_db')

    

    # parser(data)


