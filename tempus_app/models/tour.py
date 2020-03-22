from flask_sqlalchemy import SQLAlchemy
from tempus_app import db


class Tour(db.Model):
    __tablename__ = 'TOUR'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    guide_id = db.Column(db.ForeignKey('USER.id'))
    title = db.Column(db.String(32))
    description = db.Column(db.Text)
    rating = db.Column(db.Float)

    guide = db.relationship('USER', primaryjoin='TOUR.guide_id == USER.id', backref='tours')