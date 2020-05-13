from tempus_app import tempus_app, ma, db
from .models import *
from marshmallow import post_load, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow.decorators import *

class EmergencyContactSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EmergencyContact
        sqla_session = db.session
        load_instance = True

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


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

    password = auto_field(load_only=True)

    languages = fields.Nested(UserXLanguageSchema, many=True, exclude=("id",))
    emergency_contacts = fields.Nested(EmergencyContactSchema, many=True, exclude=('id',))

user_schema = UserSchema()
login_schema = UserSchema(only=('email', 'password'))

class TourImage(SQLAlchemyAutoSchema):
    class Meta:
        model = TourImage
        sqla_session = db.session
        load_instance = True


class TourSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tour
        load_instance = True
        sqla_session = db.session

    uuid = fields.UUID(dump_only=True)
    upload_time = auto_field(dump_only=True)
    duration = fields.TimeDelta(precision='minutes')
    images = fields.Nested(TourImage, many=True, exclude=('image',))

tour_schema = TourSchema()
tours_schema = TourSchema(many=True)