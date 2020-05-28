import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'imULe11*jU'
    DATABASE_PASSWORD = 'password'
    SQLALCHEMY_DATABASE_URI = 'postgresql://tempus:'+DATABASE_PASSWORD+':@45.76.120.177:5432/tempus'