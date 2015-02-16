import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
