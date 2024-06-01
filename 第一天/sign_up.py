database={}
def find_id(database,user_id):
    if user_id in database:
        print(f"{user_id}:{database[user_id]['username']}")


def look(database,username):
    for i in database:
        if database[i]['username'] == username:
            print('存在')
        else:
            print('不在')


def login(database,username,password):
    for user_id in database:
        if database[user_id]['username'] == username:
            if database[user_id]['password'] == password:
                print('登陆成功！')
            else:
                print('登陆失败！')
        else:
            print('登陆失败！')
        