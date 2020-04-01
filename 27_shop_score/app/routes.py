import pytz
from datetime import datetime

from flask import render_template
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, Query
from sqlalchemy.ext.declarative import declarative_base

from app import app
from config import POSTGRES
from app.models import Order


def get_engine():
    conn_string = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        POSTGRES["user"],
        POSTGRES["password"],
        POSTGRES["host"],
        POSTGRES["database"]
    )
    engine = create_engine(conn_string)
    return engine


def get_processed_today_orders_amount(db_session):
    today = datetime.now().replace(hour=0, minute=0, second=0)
    processed_today = db_session.query(Order).filter(
        Order.status=='COMPLETED').filter(Order.created>=today).count()
    return processed_today


def get_color(time_created):
    moscow_tz = pytz.timezone('Europe/Moscow')
    now = moscow_tz.localize(datetime.now())
    time_created = moscow_tz.localize(time_created)
    time_diff = int((now - time_created).total_seconds() / 60.0)
    color = 'LightPink'
    if time_diff < 7:
        color = 'Aquamarine'
    elif time_diff < 30:
        color = 'yellow'
    return color


def get_consolidated_orders_data(
    orders, orders_amount, today_orders_amount
):
    consolidated_orders_data = {
        'orders': [],
        'unprocessed': orders_amount,
        'processed_today': today_orders_amount
    }
    for order in orders.all():
        color = get_color(order.created)
        consolidated_orders_data['orders'].append(
            {'name': order.contact_name,
             'phone': order.contact_phone,
             'status': order.status,
             'created': order.created,
             'confirmed': order.confirmed,
             'price': order.price,
             'color': color
             }
        )
    return consolidated_orders_data


@app.route('/')
def score():
    engine = get_engine()
    Base = declarative_base()
    Base.metadata.reflect(engine)
    db_session = scoped_session(sessionmaker(bind=engine))
    pending_orders = db_session.query(
        Order).filter(Order.status.notin_(['CANCELED', 'COMPLETED']))
    pending_orders_amount = pending_orders.count()
    processed_today_orders_amount = get_processed_today_orders_amount(
        db_session
    )
    consolidated_orders_data = get_consolidated_orders_data(
        pending_orders,
        pending_orders_amount,
        processed_today_orders_amount
    )
    return render_template('score.html', orders=consolidated_orders_data)
