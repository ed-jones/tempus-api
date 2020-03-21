import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'imULe11*jU'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mQ84*!A@149.28.179.78:5432/csci334'