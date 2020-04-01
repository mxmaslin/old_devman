from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    contact_name = Column(String(200), nullable=True)
    contact_phone = Column(String(100), nullable=True)
    contact_email = Column(String(150), nullable=True)
    status = Column(String(100), nullable=False, default='', index=True)
    created = Column(DateTime(timezone=False), index=True, nullable=False)
    confirmed = Column(
        DateTime(timezone=False), index=True, nullable=True, default=''
    )
    comment = Column(Text, nullable=True)
    price = Column(Numeric, nullable=True)
