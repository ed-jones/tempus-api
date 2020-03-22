from tempus_app import tempus_app, models, api, db
from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify, request

class AddUser(Resource):
    def post(self):
        user_data = request.get_json()

        new_user = models.User(email=user_data['email'], password=user_data['password'])

        db.session.add(new_user)
        db.session.commit()

        return 'Done', 201
