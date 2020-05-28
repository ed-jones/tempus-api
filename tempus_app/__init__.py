__version__ = '0.1.0'

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow 
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS


# Setup App
tempus_app = Flask(__name__)
tempus_app.config.from_object(Config)

# Setup API
api = Api(tempus_app)

# Setup DB
db = SQLAlchemy()
db.init_app(tempus_app)
migrate = Migrate(tempus_app, db)

# Setup BCrypt
bcrypt = Bcrypt(tempus_app)

# Setup Marshmallow
ma = Marshmallow(tempus_app)

# Setup CORS
cors = CORS(tempus_app, resources={r"*": {"origins": "tempus.tours"}})

# Import views
from . import paths
