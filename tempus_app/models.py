from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy import func
from math import pi
from uuid import uuid4
from tempus_app import db
from datetime import datetime
import enum

class Language(db.Model):
    __tablename__ = 'LANGUAGE'

    id = db.Column(db.String(5), primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)

    languages = db.relationship("UserXLanguage", back_populates="language")

class Location(db.Model):
    __tablename__ = 'LOCATION'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(60))
    address = db.Column(db.String(60))
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    tour = db.relationship("Tour", uselist=False, back_populates="location")

class TourCategory(enum.Enum):
    ANIMALS = "Animals"
    BEACH = "Beach"
    FOODANDDRINK = "Food and Drink"
    HIKING = "Hiking"
    CITY = "City"

class Tour(db.Model):
    __tablename__ = 'TOUR'

    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid4)
    guide_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    upload_time = db.Column(db.DateTime, default=datetime.now)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Interval, nullable=False)
    category = db.Column(db.Enum(TourCategory), nullable=False)
    location_id = db.Column(db.ForeignKey('LOCATION.id'))
    image_url = db.Column(db.Text)
    equipment = db.Column(db.Text)
    itinerary = db.Column(db.Text)
    
    location = db.relationship("Location", back_populates="tour")
    guide = db.relationship("User", back_populates="tour")

    @hybrid_method
    def get_distance(self, user_lat, user_lng):
        pi180 = pi / 180
        lat1 = float(user_lat) * pi180
        lng1 = float(user_lng) * pi180
        lat2 = Location.lat * pi180
        lng2 = Location.lng * pi180
        r = 6371
        dlat = lat2 - lat1
        dlng = lng2 - lng1
        a = func.sin(dlat/2) * func.sin(dlat/2) + func.cos(lat1) * func.cos(lat2) * func.sin(dlng/2) * func.sin(dlng/2)
        c = 2 * func.atan2(func.sqrt(a), func.sqrt(1 - a))
        km = r * c

        return km

class ReviewType(enum.Enum):
    FROM_HOSTS = "From Hosts"
    FROM_GUESTS = "From Guests"

class Review(db.Model):
    __tablename__ = 'REVIEW'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    reviewee_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)
    reviewer_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)
    tour_id = db.Column(db.ForeignKey('TOUR.uuid'), nullable=False)
    review_type = db.Column(db.Enum(ReviewType), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'USER'

    uuid = db.Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid4)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    firstname = db.Column(db.String(32), nullable=False)
    lastname = db.Column(db.String(32), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    mobile = db.Column(db.String(15))
    customer_rating = db.Column(db.Float)
    customer_rating_count = db.Column(db.Integer, default=0)
    guide_rating = db.Column(db.Float)
    guide_rating_count = db.Column(db.Integer, default=0)
    bio = db.Column(db.Text)
    photo = db.Column(db.String(60))
    banner = db.Column(db.Text)
    website = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.now)
    location = db.Column(db.Text)

    reviews_of_me = db.relationship("Review", backref="reviewee", foreign_keys='Review.reviewee_id')
    reviews_by_me = db.relationship("Review", backref="reviewer", foreign_keys='Review.reviewer_id')
    
    languages = db.relationship("UserXLanguage", back_populates="user")
    emergency_contacts = db.relationship("EmergencyContact", back_populates="user")
    tour = db.relationship("Tour", back_populates="guide")

class EmergencyContact(db.Model):
    __tablename__ = 'EMERGENCY_CONTACT'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    homephone = db.Column(db.String(32))
    mobilephone = db.Column(db.String(32))
    workphone = db.Column(db.String(32))
    address = db.Column(db.Text)

    user = db.relationship("User", back_populates="emergency_contacts")

class UserXLanguage(db.Model):
    __tablename__ = 'USER_X_LANGUAGE'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    language_id = db.Column(db.ForeignKey('LANGUAGE.id'), nullable=False)
    user_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)

    user = db.relationship("User", back_populates="languages")
    language = db.relationship("Language", back_populates="languages")

class TourDate(db.Model):
    __tablename__ = 'TOUR_DATE'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tour_id = db.Column(db.ForeignKey('TOUR.uuid'), nullable=False)
    tour_datetime = db.Column(db.DateTime, nullable=False)

class Currency(db.Model):
    __tablename__ = 'CURRENCY'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    currency_name = db.Column(db.Text, nullable=False)
    entity = db.Column(db.Text, nullable=False)
    alpha_code = db.Column(db.String(10))
    num_code = db.Column(db.Integer)

