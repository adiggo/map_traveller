from api import db
from api.model import User
from datetime import datetime

db.create_all()

db.session.add(User("li", "adiggo@gmail.com", "pass", 2, None, None, None,datetime.now(), datetime.now()))

db.session.commit()
