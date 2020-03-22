from flask_sqlalchemy import SQLAlchemy
from tempus_app import db


class Vernacular(db.Model):
    __tablename__ = 'VERNACULAR'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    language_id = db.Column(db.ForeignKey('LANGUAGE.id'), nullable=False)
    user_id = db.Column(db.ForeignKey('USER.id'), nullable=False)

    language = db.relationship('LANGUAGE', primaryjoin='VERNACULAR.language_id == LANGUAGE.id', backref='vernaculars')
    user = db.relationship('USER', primaryjoin='VERNACULAR.user_id == USER.id', backref='vernaculars')
