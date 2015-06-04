import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../../db')
from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Table, ForeignKey

class Place(Base):

    __tablename__ = "places"

    id = Column('id', BigInteger, primary_key=True)
    city = Column('city', String(length = 200), nullable=False)
    state = Column('state', String(length = 200), nullable = False)
    country = Column('country', String(length = 200), nullable = False)
    continent = Column('continent', String(length = 200), nullable = False)

    def __init__(self, city, state, country, continent):
        self.city = city
        self.state = state
        self.country = country
        self.continent = continent