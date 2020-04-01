import argparse
import datetime
import os
import time

import phonenumbers

from sqlalchemy import create_engine
from sqlalchemy.exc import TimeoutError, DBAPIError, DisconnectionError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import sys
from os import path
sys.path.append(path.dirname(path.dirname( path.abspath(__file__))))

from app.models import Order


def get_engine():
    conn_string = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'orders'),
        os.getenv('DB_PASSWORD', '666'),
        os.getenv('DB_HOST', '127.0.0.1'),
        os.getenv('DB_NAME', 'orders')
    )
    engine = create_engine(conn_string)
    return engine


def get_some_minutes_earlier(minutes_to_wait):
    some_minutes_delta = datetime.timedelta(minutes=minutes_to_wait)
    now = datetime.datetime.now()
    some_minutes_earlier = now - some_minutes_delta
    return some_minutes_earlier


def get_national_phone_number(raw_phone_number):
    national_phone_number = ''
    try:
        phone_number_obj = phonenumbers.parse(raw_phone_number, 'RU')
        national_phone_number = phone_number_obj.national_number
    except phonenumbers.phonenumberutil.NumberParseException:
        pass
    return national_phone_number


def write_national_phone_numbers_to_db(db_session, orders):
    for order in orders:
        if order.normalized_phone:
            continue
        raw_phone_number = order.contact_phone
        national_phone_number = get_national_phone_number(raw_phone_number)
        order.normalized_phone = national_phone_number
    db_session.commit()


def normalize_existing_phonenumbers(db_session):
    existing_orders = db_session.query(Order).all()
    write_national_phone_numbers_to_db(db_session, existing_orders)


def is_normalize_existing_needed():
    parser = argparse.ArgumentParser(
        description='Convert existing phone numbers to national format'
    )
    parser.add_argument('--clear', action='store_true')
    parser_args = parser.parse_args()
    return parser_args.clear


if __name__ == '__main__':
    minutes_to_wait = 10
    seconds_to_wait = minutes_to_wait * 60
    engine = get_engine()
    Base = declarative_base()
    Base.metadata.reflect(engine)
    db_session = scoped_session(sessionmaker(bind=engine))
    normalize_existing_needed = is_normalize_existing_needed()
    if normalize_existing_needed:
        normalize_existing_phonenumbers(db_session)
    while True:
        some_minutes_earlier = get_some_minutes_earlier(minutes_to_wait)
        recent_orders = []
        try:
            recent_orders = db_session.query(Order).filter(
                Order.created >= some_minutes_earlier
            ).all()
            write_national_phone_numbers_to_db(db_session, recent_orders)
        except (TimeoutError, DBAPIError, DisconnectionError):
            db_session.rollback()
        time.sleep(seconds_to_wait)
