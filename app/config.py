import os

class Config(object):
    pass

class ProductionConfig(Config):
    db_user = os.getenv('DB_ENV_POSTGRES_USER')
    db_password = os.getenv('DB_ENV_POSTGRES_PASSWORD')
    db_host = os.getenv('DB_PORT_5432_TCP_ADDR')
    db_port = os.getenv('DB_PORT_5432_TCP_PORT')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}'.format(
            db_user, db_password, db_host, db_port)


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
