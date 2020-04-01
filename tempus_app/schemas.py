from tempus_app import tempus_app, ma
from .models import User, Tour
from marshmallow import post_load, fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    uuid = fields.UUID(dump_only=True)
    email = auto_field()
    password = auto_field(load_only=True)
    firstname = auto_field()
    lastname = auto_field()
    firstname = auto_field()
    customer_rating = auto_field()
    guide_rating = auto_field()
    mobile = auto_field()
    bio = auto_field()

user_schema = UserSchema()

class TourSchema(SQLAlchemySchema):
    class Meta:
        model = Tour
        load_instance = True

    uuid = fields.UUID(dump_only=True)
    guide_id = auto_field()
    title = auto_field()
    description = auto_field()
    rating = auto_field()
    upload_time = auto_field(dump_only=True)
    price = auto_field()
    duration = fields.TimeDelta(precision='minutes')


tour_schema = TourSchema()
tours_schema = TourSchema(many=True)