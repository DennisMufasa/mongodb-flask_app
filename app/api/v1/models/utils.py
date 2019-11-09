'''utility functions used in the models'''

import re

def password_checker(password):
    '''a function to check user passwords'''
    # check length
    if len(password) > 12 or len(password) < 6:
        return 'password error'
    return 'password ok'

def email_checker(email):
    '''a function to check for an @ in the email'''
    if bool(re.search(r'[@]', email)) is False:
        return 'email error'
    return 'email ok'


# set up the database


# third-party import
import pymongo
import datetime



class Database:
    '''a class to manage the database configurations'''
    def __init__(self):
        client = pymongo.MongoClient('mongodb://localhost:27017')
        database = client['flaskapp']
        self.users = database['users']
        self.comments = database['comments']



# populate the collections with documents
# this is the code that creates  the database, collections and documents

# add admin
# user1 = {
#     "username" : "admin",
#     "password" : "gn-z11",
#     "role" : "admin"
# }

# timestamp
timestamp = '''{}:{}:{} - {}/{}/{}'''.format(
    datetime.datetime.now().hour,
    datetime.datetime.now().minute,
    datetime.datetime.now().second,
    datetime.datetime.now().day,
    datetime.datetime.now().month,
    datetime.datetime.now().year
)

# admin's comment
# admin_comment = {
#     "comment" : "Welcome to my app!",
#     "time" : timestamp,
#     "owner" : "admin"
# }

# create documents
# insert_admin = users.insert_one(user1)
# insert_admin_comment = comments.insert_one(admin_comment)

# print(insert_admin.inserted_id)
# print(insert_admin_comment.inserted_id)