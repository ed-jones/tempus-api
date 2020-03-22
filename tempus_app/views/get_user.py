from tempus_app import tempus_app, models, api, db
from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify, request

class GetUser(Resource):
    def post(self):
        uuid_data = request.get_json()

        user_list = models.User.query.all()

        user_json = {}

        for user in user_list:
            if (str(user.uuid) == uuid_data['uuid']):
                user_json = jsonify(email=user.email, firstname=user.firstname, lastname=user.lastname, customer_rating=user.customer_rating, guide_rating=user.guide_rating, bio=user.bio)

        return user_json
