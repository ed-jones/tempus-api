__version__ = '0.1.0'

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

tempus_app = Flask(__name__)
tempus_app.config.from_object(Config)


db = SQLAlchemy()
db.init_app(tempus_app)


from .views import main
tempus_app.register_blueprint(main)

