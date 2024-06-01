import time
from sign_in import *
from sign_up import *


#1233333
database = {}
username = input
password = input


database,user_id = reg(database, username, password, '3')
time.sleep(2)

find_id(database,user_id)
time.sleep(2)

login(database, username,password)
time.sleep(2)

