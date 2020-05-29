from tempus_app import tempus_app, ma, db
from .models import *
from marshmallow import post_load, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow.decorators import *
from marshmallow_enum import EnumField

class EmergencyContactSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EmergencyContact
        sqla_session = db.session
        load_instance = True

class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        sqla_session = db.session
        load_instance = True

    review_type = EnumField(ReviewType)

class LanguageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Language
        sqla_session = db.session
        load_instance = True

    name = auto_field()
    id = auto_field()

class UserXLanguageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserXLanguage
        sqla_session = db.session
        load_instance = True

    user_id = fields.UUID(load_only=True)
    language_id = auto_field(load_only=True)
    language = fields.Nested(LanguageSchema)

user_x_language_schema = UserXLanguageSchema()


class Location(SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        sqla_session = db.session
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

    password = auto_field(load_only=True)
    languages = fields.Nested(UserXLanguageSchema, many=True, exclude=("id",))
    emergency_contacts = fields.Nested(EmergencyContactSchema, many=True, exclude=('id',))

    reviews_of_me = fields.Nested(ReviewSchema, many=True)
    reviews_by_me = fields.Nested(ReviewSchema, many=True)


user_schema = UserSchema()
login_schema = UserSchema(only=('email', 'password'))

class TourSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tour
        load_instance = True
        sqla_session = db.session

    uuid = fields.UUID(dump_only=True)
    upload_time = auto_field(dump_only=True)
    duration = fields.TimeDelta(precision='minutes')
    location = fields.Nested(Location)
    category = EnumField(TourCategory)
    guide = fields.Nested(UserSchema)

tour_schema = TourSchema()
tours_schema = TourSchema(many=True)