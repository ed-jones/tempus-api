from flask_sqlalchemy import SQLAlchemy
from tempus_app import db


class Location(db.Model):
    __tablename__ = 'LOCATION'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    tour_id = db.Column(db.ForeignKey('TOUR.id'))
    name = db.Column(db.String(60))
    address = db.Column(db.String(60))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    tour = db.relationship('TOUR', primaryjoin='LOCATION.tour_id == TOUR.id', backref='locations')
