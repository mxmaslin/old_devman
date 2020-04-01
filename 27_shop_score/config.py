import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


POSTGRES = {
    'user': 'score',
    'password': 'Rysherat2',
    'database': 'shop',
    'host': 'shopscore.devman.org',
    'port': '5432'
}