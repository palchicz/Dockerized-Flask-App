import os

class Config(object):
    db_user = os.environ['DB_ENV_POSTGRES_USER']
    db_password = os.environ['DB_ENV_POSTGRES_PASSWORD']
    db_host = os.environ['DB_PORT_5432_TCP_ADDR']
    db_port = os.environ['DB_PORT_5432_TCP_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}'.format(
            db_user, db_password, db_host, db_port)
