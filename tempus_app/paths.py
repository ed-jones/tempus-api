from tempus_app import tempus_app, api, db, bcrypt
from flask import jsonify, request, send_file
from flask_restful import abort, Api, Resource
from sqlalchemy import asc, desc, func
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

import io
from math import pi, sin, cos, atan2, sqrt
from datetime import datetime, timedelta
from uuid import UUID, uuid4
from datetime import timedelta

from .models import User, Tour, Location, TourCategory
from .schemas import user_schema, tour_schema, tours_schema, login_schema, user_x_language_schema

class GetTours(Resource):
    def get(self):
        args = request.args
        tours = Tour.query.join(Tour.location)

        DEFAULT_NUM = 4

        if 'order_by' in args:

            if args['order_by'] == 'distance' and 'lat' in args and 'lng' in args:
                order_by_value = Tour.get_distance(args['lat'], args['lng'])
            else:
                order_by_value = getattr(Tour, args['order_by'])

            if 'sort' in args:
                if args['sort'] == 'asc':
                    order_by_value = asc(order_by_value)
                elif args['sort'] == 'desc':
                    order_by_value = desc(order_by_value)
            else:
                order_by_value = asc(order_by_value)

            tours = tours.order_by(order_by_value)

        if 'category' in args:
            tours = tours.filter(Tour.category == getattr(TourCategory, args['category']))

        if 'lat' in args and 'lng' in args:
            if 'max_distance' in args:
                tours = tours.filter(Tour.get_distance(args['lat'], args['lng']) <= int(args['max_distance']))

            if 'min_distance' in args:
                tours = tours.filter(Tour.get_distance(args['lat'], args['lng']) >= int(args['min_distance']))
                        
        if 'max_rating' in args:
            tours = tours.filter(Tour.rating <= float(args['max_rating']))

        if 'min_rating' in args:
            tours = tours.filter(Tour.rating >= float(args['min_rating']))

        if 'max_upload_time' in args:
            tours = tours.filter(Tour.upload_time <= datetime.fromtimestamp(int(args['max_upload_time'])))

        if 'min_upload_time' in args:
            tours = tours.filter(Tour.upload_time >= datetime.fromtimestamp(int(args['min_upload_time'])))

        if 'max_duration' in args:
            tours = tours.filter(Tour.duration <= timedelta(minutes=int(args['max_duration'])))

        if 'min_duration' in args:
            tours = tours.filter(Tour.duration >= timedelta(minutes=int(args['min_duration'])))

        if 'max_price' in args:
            tours = tours.filter(Tour.price <= float(args['max_price']))

        if 'min_price' in args:
            tours = tours.filter(Tour.price >= float(args['min_price']))
                    
        if 'num' in args:
            num = int(args['num'])

        tours = tours.limit(DEFAULT_NUM)

        if 'page' in args:
            tours = tours.offset(DEFAULT_NUM*(int(args['page'])-1))

        return tours_schema.dump(tours), 200
api.add_resource(GetTours, '/tours')

class GetTour(Resource):
    def get(self, uuid):
        try:
            UUID(uuid, version=1)
        except ValueError:
            abort(400, message="Invalid UUID Supplied")

        tour = Tour.query.filter_by(uuid=uuid).first()

        if (not tour):
            abort(400, message="Tour not found")

        return tour_schema.dump(tour), 200

    @jwt_required
    def put(self, uuid):
        if uuid != get_jwt_identity():
            return 'Authentication Error', 401

        tour_data = tour_schema.load(request.get_json())

        try:
            UUID(uuid, version=1)
        except ValueError:
            abort(400, message="Invalid UUID Supplied")

        tour = Tour.query.filter_by(uuid=uuid)

        if (not tour):
            abort(404, message="Tour not found") 

        tour.update(tour_data)
        db.session.commit()
        return 'Tour successfully updated', 200

    @jwt_required
    def delete(self, uuid):
        if uuid != get_jwt_identity():
            return 'Authentication Error', 401

        try:
            UUID(uuid, version=1)
        except ValueError:
            abort(400, "Invalid UUID Supplied") 

        tour = Tour.query.filter_by(uuid=uuid)

        if (not tour.first()):
            abort(404, message="Tour not found")

        tour.delete()
        db.session.commit()
        return 'Tour successfully deleted', 200
api.add_resource(GetTour, '/tour/<string:uuid>')

class AddTour(Resource):
    @jwt_required
    def post(self):
        new_tour = tour_schema.load(request.get_json())

        if new_tour.guide_id != get_jwt_identity():
            return 'Authentication Error', 401

        db.session.add(new_tour)
        db.session.commit()

        return 'Done', 201
api.add_resource(AddTour, '/tour')

class AddUser(Resource):
    def post(self):
        user_id = uuid4()
        user_data = request.get_json()
        user_data['uuid'] = user_id
        user_data['password'] = bcrypt.generate_password_hash(user_data['password'])
        new_user = user_schema.load(user_data)
        db.session.add(new_user)
        db.session.commit()

        return 'Done', 201

api.add_resource(AddUser, '/user/add')

class GetUser(Resource):
    def get(self, uuid):

        try:
            UUID(uuid, version=1)
        except ValueError:
            abort(400, message="Invalid UUID Supplied")

        user = User.query.filter_by(uuid=uuid).first()

        if (not user):
            abort(404, message="User not found")

        return user_schema.dump(user), 200

    @jwt_required
    def put(self, uuid):

        user_data = user_schema.load(request.get_json())

        if user_data.uuid != get_jwt_identity():
            return 'Authentication Error', 401

        try:
            UUID(uuid, version=1)
        except ValueError:
            abort(400, message="Invalid UUID Supplied")

        user = User.query.filter_by(uuid=uuid)

        if (not user):
            abort(404, message="User not found")

        user.update(user_data)
        db.session.commit()
        return 'User successfully updated', 200

    @jwt_required
    def delete(self, uuid):

        if uuid != get_jwt_identity():
            return 'Authentication Error', 401

        try:
            UUID(uuid, version=1)
        except ValueError:
            abort(400, message="Invalid UUID Supplied")

        user = User.query.filter_by(uuid=uuid)

        if (not user.first()):
            abort(400, message="User not found")

        user.delete()
        db.session.commit()

        return 'User successfully deleted', 200
api.add_resource(GetUser, '/user/<string:uuid>')

class LoginUser(Resource):
    def post(self):
        user_data = login_schema.load(request.get_json())

        user = User.query.filter_by(email=user_data.email).first()

        if (not user or not bcrypt.check_password_hash(user.password, user_data.password)):
            abort(401, message="Invalid username/password supplied")

        access_token = create_access_token(identity=user.uuid)

        return {"token": access_token, "user": user_schema.dump(user_data)}, 200

api.add_resource(LoginUser, '/user/login')

# Not sure if this is necessary any more
class LogoutUser(Resource): 
    def get(self):

        return 'Successfully logged out', 200
api.add_resource(LogoutUser, '/user/logout')

class Me(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()

        user = User.query.filter_by(uuid=current_user).first()

        if (not user):
            abort(404, message="User not found")

        return user_schema.dump(user), 200

api.add_resource(Me, '/user/me')

        