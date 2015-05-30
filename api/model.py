from api import db
from api import bcrypt
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))
    fid = db.Column(db.String(200))
    wid = db.Column(db.String(200))
    dob = db.Column(db.DateTime)
    # need to discuss whether store it in db or file system
    profile_photo = db.Column(db.BLOB)
    create_time = db.Column(db.DateTime, nullable = False, default=func.now())
    update_time = db.Column(db.DateTime)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

class Place(db.Model):

    __tablename__ = "place"

    id = db.Column(db.BigInteger, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable = False)
    country = db.Column(db.String(100), nullable = False)
    continent = db.Column(db.String(100), nullable = False)
    def __init__(self, city, state, country, continent):
        self.city = city
        self.state = state
        self.country = country
        self.continent = continent

class UserPlaceLink(db.Model):
    __tablename__ = "user_place"
    
    user_id = db.Column(db.BigInteger, primary_key = True)
    place_id = db.Column(db.BigInteger, primary_key = True)
    def __init__(self, user_id, place_id):
        self.user_id = user_id
        self.place_id = place_id