__version__ = '0.1.0'

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow 


# Setup App
tempus_app = Flask(__name__)
tempus_app.config.from_object(Config)

# Setup API
api = Api(tempus_app)

# Setup DB
db = SQLAlchemy()
db.init_app(tempus_app)


# Setup Marshmallow
ma = Marshmallow(tempus_app)

# Import views
from . import paths


# Setup Routes
api.add_resource(paths.AddUser, '/user/')
api.add_resource(paths.GetUser, '/user/<string:uuid>')
api.add_resource(paths.RecentTours, '/recent_tours')
api.add_resource(paths.NearestTours, '/nearest_tours')