import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'me-is-so-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL'
    ) or 'sqlite:///' + os.path.join(basedir, 'realty.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADS_PER_PAGE = 15
