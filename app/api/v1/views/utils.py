'''helper functions for the views'''

import re

def check_user_data(user_data):
    '''a function to ensure user data is all present'''

    if isinstance(user_data, dict) is False:
        return 'user data should be passed as a dictionary object'

    user_data_labels = ["username", "password", "email", "role"]

    '''check if all labels are present'''
    for i in range(len(user_data_labels)):
        if user_data_labels[i] in user_data:
            continue
        else:
            return 'Keyword {} is missing from user data'.format(user_data_labels[i])

    '''check for empty values in the user credentials'''
    for key, value in user_data.items():
        if len(value) > 0:
            continue
        else:
            return '{} is missing a value!'.format(key)

    if len(user_data['password']) > 12 or len(user_data['password']) < 6:
        return 'password length should be between 6 and 12 characters long!'
        
    if bool(re.search('[@]', user_data['email'])) is False:
        return 'Invalid email address!'
    

    return 'All user data present'