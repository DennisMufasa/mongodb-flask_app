'''execute an instance of the flask app'''
# system import
import os

# local import
from .app.api import create_app

# get environment configuration
env_config = os.getenv('ENV_CONFIG')

# create an app
app = create_app(env_config)

# run app
if __name__ == '__main__':
    app.run()
