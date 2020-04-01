from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    contact_phone = Column(String(100), nullable=True)
    normalized_phone = Column(String(100), nullable=True)
    created = Column(DateTime(timezone=False), index=True, nullable=False)
