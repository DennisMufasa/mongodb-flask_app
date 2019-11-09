# local import
from . import utils


class User(utils.Database):
    '''a model to handle user information'''
    def __init__(self):
        '''class constructor'''
        utils.Database.__init__(self)
        self.username = ""
        self.password = ""
        self.email = ""
        self.role = ""
    
    def save_user(self,username, password, email, role):
        '''save new user to the database'''
        if utils.password_checker(password) == 'password ok' and utils.email_checker(email) == 'email ok':
            self.username = username
            self.password = password
            self.email = email
            self.role = role

            # create user object - document
            user = {
                "username" : self.username,
                "password" : self.password,
                "email" : self.email,
                "role" : self.role
            }
            
            # save user data
            save_user = self.users.insert_one(user)
            return "New user saved, user_id - {}".format(save_user.inserted_id)
        utils.password_checker(password)

    def find_username(self, email):
        '''find user details using their email'''
        user_details = self.users.find({"email": email}, {"_id": 0, "password": 0})
        
        output = dict()

        for detail in user_details:
            output.update(detail)
        
        if not output:
            return 'email is not registered'
        return output

    def fetch_all_users(self):
        all_users = self.users.find({}, {"_id": 0, "password": 0})

        output = list()

        for user in all_users:
            output.append(user)
        
        if not output:
            return 'No users present'
        
        return output