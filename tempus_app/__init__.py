__version__ = '0.1.0'

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


# Setup App
tempus_app = Flask(__name__)
tempus_app.config.from_object(Config)

# Setup API
api = Api(tempus_app)

# Setup DB
db = SQLAlchemy()
db.init_app(tempus_app)

# Import views
from . import views

# Setup Routes
api.add_resource(views.AddUser, '/add_user')
api.add_resource(views.GetUser, '/get_user')

