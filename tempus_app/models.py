# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, LargeBinary, String, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from . import db



# t_LANGUAGE = db.Table(
#     'LANGUAGE',
#     db.Column('id', db.String(5), nullable=False, unique=True),
#     db.Column('name', db.String(32))
# )



# class LOCATION(db.Model):
#     __tablename__ = 'LOCATION'

#     id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
#     tour_id = db.Column(db.ForeignKey('TOUR.id'))
#     name = db.Column(db.String(60))
#     address = db.Column(db.String(60))
#     lat = db.Column(db.Float)
#     lng = db.Column(db.Float)

#     tour = db.relationship('TOUR', primaryjoin='LOCATION.tour_id == TOUR.id', backref='locations')



# class TOUR(db.Model):
#     __tablename__ = 'TOUR'

#     id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
#     guide_id = db.Column(db.ForeignKey('USER.id'))
#     title = db.Column(db.String(32))
#     description = db.Column(db.Text)
#     rating = db.Column(db.Float)

#     guide = db.relationship('USER', primaryjoin='TOUR.guide_id == USER.id', backref='tours')



# class TOURIMAGE(db.Model):
#     __tablename__ = 'TOUR_IMAGE'

#     id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
#     tour_id = db.Column(db.ForeignKey('TOUR.id'))
#     title = db.Column(db.String(32))
#     description = db.Column(db.Text)
#     date = db.Column(db.Date)
#     image = db.Column(db.LargeBinary)

#     tour = db.relationship('TOUR', primaryjoin='TOURIMAGE.tour_id == TOUR.id', backref='tourimages')

class User(db.Model):
    __tablename__ = 'USER'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    customer_rating = db.Column(db.Float)
    guide_rating = db.Column(db.Float)
    bio = db.Column(db.Text)


# t_USER = db.Table(
#     'USER',
#     db.Column('id', db.Integer, nullable=False, unique=True),
#     db.Column('email', db.String(60)),
#     db.Column('password', db.String(60)),
#     db.Column('firstname', db.String(32)),
#     db.Column('lastname', db.String(32)),
#     db.Column('customer_rating', db.Float),
#     db.Column('guide_rating', db.Float),
#     db.Column('bio', db.Text)
# )



# class VERNACULAR(db.Model):
#     __tablename__ = 'VERNACULAR'

#     id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
#     language_id = db.Column(db.ForeignKey('LANGUAGE.id'), nullable=False)
#     user_id = db.Column(db.ForeignKey('USER.id'), nullable=False)

#     language = db.relationship('LANGUAGE', primaryjoin='VERNACULAR.language_id == LANGUAGE.id', backref='vernaculars')
#     user = db.relationship('USER', primaryjoin='VERNACULAR.user_id == USER.id', backref='vernaculars')
