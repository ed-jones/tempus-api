from flask_sqlalchemy import SQLAlchemy
from tempus_app import db


class TourImage(db.Model):
    __tablename__ = 'TOUR_IMAGE'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    tour_id = db.Column(db.ForeignKey('TOUR.id'))
    title = db.Column(db.String(32))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    image = db.Column(db.LargeBinary)

    tour = db.relationship('TOUR', primaryjoin='TOURIMAGE.tour_id == TOUR.id', backref='tourimages')
