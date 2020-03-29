from tempus_app import tempus_app, models, api, db, schemas
from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify, request
from math import pi, sin, cos, atan2, sqrt
from uuid import UUID
from .models import User
from .schemas import user_schema

class NearestTours(Resource):
    def post(self):

        user_location = request.get_json()
        user_lat = user_location['lat']
        user_lng = user_location['lng']

        locations_model = models.Location.query.all()
        locations_list = []

        for location_model in locations_model:
            tour = models.Tour.query.filter_by(id={location_model.tour_id}).first()

            locations_list.append({
                "tour_id" : location_model.tour_id,
                "distance" : distance(float(user_lat), float(user_lng), location_model.lat, location_model.lng),
                })
        


        # locations_list = sorted(locations_list, key=lambda k: k['distance'])

        # nearest_tours = []
        
        # for location in locations_list:
        #     nearest_tours.append(models.Tour.query.filter_by(title == location.tour_id))

        # tours_list = []

        # for nearest_tour in nearest_tours:
        #     tours_list.append({
        #         "uuid" : str(nearest_tour.uuid), 
        #         "guide_id": nearest_tour.guide_id, 
        #         "title" : nearest_tour.title, 
        #         "description" : nearest_tour.description, 
        #         "rating" : nearest_tour.rating,
        #         "upload_time" : str(nearest_tour.upload_time),
        #         "price" : nearest_tour.price,
        #         "duration" : str(nearest_tour.duration)
        #         })

        return tours_list


def distance(lat1, lng1, lat2, lng2):
    pi180 = pi / 180
    lat1 *= pi180
    lng1 *= pi180
    lat2 *= pi180
    lng2 *= pi180

    r = 6378137
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = sin(dlat/2) * sin(dlat/2) + cos(lat1) * cos(lat2) * sin(dlng/2) * sin(dlng/2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = r * c

    return km

class RecentTours(Resource):
    def get(self):

        tours_model = models.Tour.query.order_by(models.Tour.upload_time)
        tours_list = []

        for tour_model in tours_model:
            tours_list.append({
                "uuid" : str(tour_model.uuid), 
                "guide_id": tour_model.guide_id, 
                "title" : tour_model.title, 
                "description" : tour_model.description, 
                "rating" : tour_model.rating,
                "upload_time" : str(tour_model.upload_time),
                "price" : tour_model.price,
                "duration" : str(tour_model.duration)
                })


        return tours_list


class AddUser(Resource):
    def post(self):
        user_data = request.get_json()
        new_user = user_schema.load(user_data, session=db.session)

        db.session.add(new_user)
        db.session.commit()

        return 'Done', 201

class GetUser(Resource):
    def get(self, uuid):

        try:
            UUID(uuid, version=1)
        except ValueError:
            return 'Invalid username supplied', 400

        user = User.query.filter_by(uuid=uuid).first()

        if (user):
            return user_schema.dump(user), 200
        else:
            return 'User not found', 404

    def put(self, uuid):

        user_data = request.get_json()

        try:
            UUID(uuid, version=1)
        except ValueError:
            return 'Invalid username supplied', 400

        user = User.query.filter_by(uuid=uuid)

        if (user):
            user.update(user_data)
            db.session.commit()
            return 'User successfully updated', 200
        else:
            return 'User not found', 404
            
    def delete(self, uuid):
        try:
            UUID(uuid, version=1)
        except ValueError:
            return 'Invalid username supplied', 400

        user = User.query.filter_by(uuid=uuid)

        if (user.first()):
            user.delete()
            db.session.commit()
            return 'User successfully deleted', 200
        else:
            return 'User not found', 404

class LoginUser(Resource):
    def post(self):
        user_data = request.get_json()

        user = User.query.filter_by(email=user_data["email"]).first()
        
        if (user.password == user_data["password"]):
            return 'Successfully logged in', 200
        else:
            return 'Invalid username/password supplied', 400

class LogoutUser(Resource):
    def get(self):

        return 'Successfully logged out', 200