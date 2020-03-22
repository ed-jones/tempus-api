from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from tempus_app import db


class User(db.Model):
    __tablename__ = 'USER'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    customer_rating = db.Column(db.Float)
    guide_rating = db.Column(db.Float)
    bio = db.Column(db.Text)
