from flask_sqlalchemy import SQLAlchemy
from tempus_app import db


class Language(db.Model):
    __tablename__ = 'LANGUAGE'

    id = db.Column(db.String(5), primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(32))


