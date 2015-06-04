import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../../db')
from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Table, ForeignKey

class UserPlaces(Base):
    __tablename__ = "user_places"
    
    id = Column('id', BigInteger, primary_key = True)
    user_id = Column('user_id', BigInteger, ForeignKey('users.id', name='fk_user_places_user_id'), nullable = False)
    place_id = Column('place_id', BigInteger, ForeignKey('places.id', name='fk_user_places_place_id'), nullable = False)
    started_at = Column('started_at', DateTime, nullable = False)
    left_at = Column('left_at', DateTime, nullable = False)


    def __init__(self, user_id, place_id, started_at, left_at):
        self.user_id = user_id
        self.place_id = place_id
        self.started_at = started_at
        self.left_at = left_at