'''set up the version 1 blueprint'''

# third-party import
from flask import Blueprint

# version 1 blueprint
v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

# import views
from .views import views