from api import db
from api import bcrypt
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))
    fid = db.Column(db.String(200))
    wid = db.Column(db.String(200))
    dob = db.Column(db.DateTime)
    # need to discuss whether store it in db or file system
    profile_photo = db.Column(db.BLOB)
    create_time = db.Column(db.DateTime, nullable = False, default=func.now())
    update_time = db.Column(db.DateTime)


    def __init__(self, username, email, password, fid, wid, dob, profile_photo, create_time, update_time):
        self.username = username 
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.fid = fid
        self.wid = wid
        self.dob = dob
        self.profile_photo = profile_photo
        self.create_time = create_time
        self.update_time = update_time

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


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
