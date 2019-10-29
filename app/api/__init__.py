'''Flask app factory to create a new app on invokation'''
# system import
import os

# import Flask app
from flask import Flask

# import environment configurations
from ...instance import config

def create_app(env):
    '''the app factory'''
    # create object of the app
    app = Flask(__name__,instance_relative_config=True)
    # allow instance configuration
    app.config.from_object(config.configuration[env])
    # set up secret key
    app.secret_key = os.urandom(24)

    #register blueprints to the app
    from .v1 import v1_blueprint
    app.register_blueprint(v1_blueprint)

    # initialize the object
    return app
