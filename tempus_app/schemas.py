from tempus_app import tempus_app, ma
from .models import User
from marshmallow import post_load
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    email = auto_field()
    password = auto_field()
    firstname = auto_field()
    lastname = auto_field()
    firstname = auto_field()
    customer_rating = auto_field()
    guide_rating = auto_field()
    bio = auto_field()


user_schema = UserSchema()
