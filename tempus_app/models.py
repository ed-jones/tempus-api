from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from tempus_app import db


class Language(db.Model):
    __tablename__ = 'LANGUAGE'

    id = db.Column(db.String(5), primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(32))


class Location(db.Model):
    __tablename__ = 'LOCATION'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    tour_id = db.Column(db.ForeignKey('TOUR.id'))
    name = db.Column(db.String(60))
    address = db.Column(db.String(60))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    # tour = db.relationship('TOUR', primaryjoin='LOCATION.tour_id == TOUR.id', backref='locations')

class TourImage(db.Model):
    __tablename__ = 'TOUR_IMAGE'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    tour_id = db.Column(db.ForeignKey('TOUR.id'))
    title = db.Column(db.String(32))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    image = db.Column(db.LargeBinary)

    # tour = db.relationship('TOUR', primaryjoin='TOUR_IMAGE.tour_id == TOUR.id', backref='tourimages')

class Tour(db.Model):
    __tablename__ = 'TOUR'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    guide_id = db.Column(db.ForeignKey('USER.id'))
    title = db.Column(db.String(32))
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False, server_default=db.FetchedValue())
    upload_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    price = db.Column(db.Float)
    duration = db.Column(db.Interval)

    # guide = db.relationship('USER', primaryjoin='TOUR.guide_id == USER.id', backref='tours')

class User(db.Model):
    __tablename__ = 'USER'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    customer_rating = db.Column(db.Float)
    guide_rating = db.Column(db.Float)
    bio = db.Column(db.Text)

class Vernacular(db.Model):
    __tablename__ = 'VERNACULAR'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    language_id = db.Column(db.ForeignKey('LANGUAGE.id'), nullable=False)
    user_id = db.Column(db.ForeignKey('USER.id'), nullable=False)

    #language = db.relationship('LANGUAGE', primaryjoin='VERNACULAR.language_id == LANGUAGE.id', backref='vernaculars')
    #user = db.relationship('USER', primaryjoin='VERNACULAR.user_id == USER.id', backref='vernaculars')
