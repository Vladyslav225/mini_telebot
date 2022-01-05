from finder_models import DataParsing, DataUser

from finder_parser import parser


def user_response_save_db(id_user, text_search):


    print('user_response_save_db')

    a = DataUser(user_chat_id=id_user, query=text_search)

    if text_search in a:
        print(123)
    a.save()

    for data in DataUser.objects:
        parser(data.query)

# def parsing_answer_save_db(answer):

#     print('parsing_answer_save_db')

    # parser(answer)



