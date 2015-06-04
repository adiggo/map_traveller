import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../../db')
from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Table, ForeignKey

class User(Base):

    __tablename__ = "user"

    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String(length=200), nullable=False)
    email = Column('email', String(length=200))
    password = Column('password', String(length=200))
    fid = Column('fid', String(length=200))
    wid = Column('wid', String(length=200))
    date_of_birth = Column('date_of_birth', DateTime)
    profile_photo = Column('profile_photo', String(length=200))
    created_at = Column('created_at', DateTime, nullable=False)
    updated_at = Column('updated_at', DateTime, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)