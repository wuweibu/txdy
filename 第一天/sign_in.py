import random

def reg(database,username,password,level):
    user_id = str(random.randint(1,100))
    database[user_id] = {'username':username,
                         'password':password,
                         'level':level}
    print(f'user {username} has already been record,user id is {user_id}')
    for i in database:
        print(database[i]['password'])
    return database,user_id


reg(database={},username='wwb',password=123123,level=5)