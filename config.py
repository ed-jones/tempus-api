import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'imULe11*jU'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mQ84*!A@149.28.179.78:5432/csci334'
    SQLALCHEMY_DATABASE_URI = 'postgresql://tempus:%yLb36Bs2G@127.0.0.1:5432/tempus'