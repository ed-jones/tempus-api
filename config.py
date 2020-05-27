import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'imULe11*jU'
    DATABASE_PASSWORD = '%yLb36Bs2G'
    SQLALCHEMY_DATABASE_URI = 'postgresql://tempus:'+DATABASE_PASSWORD+':@127.0.0.1:5432/tempus'