'''API endpoints'''
# system import
import os

# third-party imports
from flask import request, jsonify, make_response



# local imports
from ..models.users import User
from .. import v1_blueprint
from .import utils


# endpoints
@v1_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    '''create a new user'''
    if request.method == 'POST':
        request_data = request.get_json()

        '''check presence of registration data'''
        if not request_data:
            return make_response(jsonify({"message": 'Enter user credentials to register!'}), 406)

        #check if captured user data is all present
        if 'All user data present' == utils.check_user_data(request_data):
            new_user = User()
            add_user = new_user.save_user(request_data['username'],
            request_data['password'],request_data['email'],request_data['role'])

            # response
            return make_response(jsonify({"Response": add_user}), 201)
        else:
            keyword_error = utils.check_user_data(request_data)
            return make_response(jsonify({'Response': keyword_error}), 406)

    return make_response(jsonify({"Response": "This is where you create and save a user to the database"}), 200)

# @v1_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         request_data = request.get_json()

#         '''check for presence of data'''
#         if not request_data:
#             return "Enter user credentials to login!"
        