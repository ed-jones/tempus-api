from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from tempus_app import db
from datetime import datetime
import enum

class Language(db.Model):
    __tablename__ = 'LANGUAGE'

    id = db.Column(db.String(5), primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)

class TourLocation(db.Model):
    __tablename__ = 'TOUR_LOCATION'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tour_id = db.Column(db.ForeignKey('TOUR.uuid'), nullable=False)
    name = db.Column(db.String(60))
    address = db.Column(db.String(60))
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

class TourImage(db.Model):
    __tablename__ = 'TOUR_IMAGE'
    __table_args__ = (db.UniqueConstraint('primary', 'tour_id', name="primary_image_constraint"),)

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tour_id = db.Column(db.ForeignKey('TOUR.uuid'), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    primary = db.Column(db.Boolean)

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
    category = db.Column(db.ARRAY(db.Enum(TourCategory)), nullable=False)

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
    photo = db.Column(db.LargeBinary)
    url = db.Column(db.String(60))
    date_created = db.Column(db.DateTime, default=datetime.now)
    location = db.Column(db.Text)

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

class UserXLanguage(db.Model):
    __tablename__ = 'USER_X_LANGUAGE'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    language_id = db.Column(db.ForeignKey('LANGUAGE.id'), nullable=False)
    user_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)

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

class ReviewType(enum.Enum):
    GUIDE = "Guide"
    CUSTOMER = "Customer"

class Review(db.Model):
    __tablename__ = 'REVIEW'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    reviewer_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)
    reviewee_id = db.Column(db.ForeignKey('USER.uuid'), nullable=False)
    tour_id = db.Column(db.ForeignKey('TOUR.uuid'), nullable=False)
    review_type = db.Column(db.Enum(ReviewType), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text)
