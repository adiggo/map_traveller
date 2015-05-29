from api import db


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class user(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40))
    password = db.Column(db.String(40))
    fid = db.Column(db.String(40))
    wid = db.Column=(db.String(40))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password




