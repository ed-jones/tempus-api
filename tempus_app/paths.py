from tempus_app import tempus_app, api, db, bcrypt
from flask import jsonify, request, send_file
from flask_restful import abort, Api, Resource
from sqlalchemy import asc, desc
import io

from math import pi, sin, cos, atan2, sqrt
from datetime import datetime, timedelta
from uuid import UUID, uuid4

from .models import User, Tour, TourImage
from .schemas import user_schema, tour_schema, tours_schema, login_schema, user_x_language_schema

class AddTour(Resource):
    def post(self):
        new_tour = tour_schema.load(request.get_json())
        db.session.add(new_tour)
        db.session.commit()

        return 'Done', 201
api.add_resource(AddTour, '/tour')

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

    def put(self, uuid):
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

    def delete(self, uuid):
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

class GetTours(Resource):
    def get(self):
        args = request.args
        tours = Tour.query

        if 'order_by' in args:
            order_by_value = getattr(Tour, args['order_by'])

            if 'sort' in args:
                if args['sort'] == 'asc':
                    order_by_value = asc(order_by_value)
                elif args['sort'] == 'desc':
                    order_by_value = desc(order_by_value)

            tours = tours.order_by(order_by_value)

        if 'no' in args:
            tours = tours.limit(int(args['no']))
        else:
            tours = tours.limit(4)

        return tours_schema.dump(tours), 200
api.add_resource(GetTours, '/tours')

class GetTourImage(Resource):
    def get(self, uuid):
        image_binary = TourImage.query.filter_by(uuid=uuid).first().image

        return send_file(
            io.BytesIO(image_binary),
            mimetype='image/jpeg',
            attachment_filename='%s.jpg')
            
api.add_resource(GetTourImage, '/media/<string:uuid>/')


# class NearestTours(Resource):
#     def post(self):

#         user_location = request.get_json()
#         user_lat = user_location['lat']
#         user_lng = user_location['lng']

#         locations_model = models.Location.query.all()
#         locations_list = []

#         for location_model in locations_model:
#             tour = models.Tour.query.filter_by(id={location_model.tour_id}).first()

#             locations_list.append({
#                 "tour_id" : location_model.tour_id,
#                 "distance" : distance(float(user_lat), float(user_lng), location_model.lat, location_model.lng),
#                 })
        


#         # locations_list = sorted(locations_list, key=lambda k: k['distance'])

#         # nearest_tours = []
        
#         # for location in locations_list:
#         #     nearest_tours.append(models.Tour.query.filter_by(title == location.tour_id))

#         # tours_list = []

#         # for nearest_tour in nearest_tours:
#         #     tours_list.append({
#         #         "uuid" : str(nearest_tour.uuid), 
#         #         "guide_id": nearest_tour.guide_id, 
#         #         "title" : nearest_tour.title, 
#         #         "description" : nearest_tour.description, 
#         #         "rating" : nearest_tour.rating,
#         #         "upload_time" : str(nearest_tour.upload_time),
#         #         "price" : nearest_tour.price,
#         #         "duration" : str(nearest_tour.duration)
#         #         })

#         return tours_list


# def distance(lat1, lng1, lat2, lng2):
#     pi180 = pi / 180
#     lat1 *= pi180
#     lng1 *= pi180
#     lat2 *= pi180
#     lng2 *= pi180

#     r = 6378137
#     dlat = lat2 - lat1
#     dlng = lng2 - lng1
#     a = sin(dlat/2) * sin(dlat/2) + cos(lat1) * cos(lat2) * sin(dlng/2) * sin(dlng/2)
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     km = r * c

#     return km

# class RecentTours(Resource):
#     def get(self):

#         tours_model = models.Tour.query.order_by(models.Tour.upload_time)
#         tours_list = []

#         for tour_model in tours_model:
#             tours_list.append({
#                 "uuid" : str(tour_model.uuid), 
#                 "guide_id": tour_model.guide_id, 
#                 "title" : tour_model.title, 
#                 "description" : tour_model.description, 
#                 "rating" : tour_model.rating,
#                 "upload_time" : str(tour_model.upload_time),
#                 "price" : tour_model.price,
#                 "duration" : str(tour_model.duration)
#                 })


#         return tours_list

class AddUser(Resource):
    def post(self):
        user_id = uuid4()

        user_data = request.get_json()
        # languages_data = user_data['languages']

        # user_data.pop('languages')
        user_data['uuid'] = user_id
        user_data['password'] = bcrypt.generate_password_hash(user_data['password'])
        new_user = user_schema.load(user_data)
        db.session.add(new_user)


        # for language_data in languages_data:
        #     language_data['user_id'] = user_id
        #     new_language_relation = user_x_language_schema.load(language_data)
        #     db.session.add(new_language_relation)

        db.session.commit()

        return 'Done', 201

api.add_resource(AddUser, '/user/')

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


    def put(self, uuid):

        user_data = user_schema.load(request.get_json())

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
            
    def delete(self, uuid):
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
            abort(400, message="Invalid username/password supplied")

        return 'Successfully logged in', 200
api.add_resource(LoginUser, '/user/login')

class LogoutUser(Resource):
    def get(self):

        return 'Successfully logged out', 200
api.add_resource(LogoutUser, '/user/logout')
