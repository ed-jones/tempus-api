from tempus_app import tempus_app
from flask import render_template, Blueprint, jsonify, request
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()

    new_user = User(email=user_data['email'], password=user_data['password'])

    db.session.add(new_user)
    db.session.commit()

    return 'Done', 201

@main.route('/users')
def users():
    user_list = User.query.all()
    users = []

    for user in user_list:
        users.append({'email' : user.email, 'password' : user.password})


    return jsonify({'users' : users})