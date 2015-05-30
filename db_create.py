from api import db
from api.model import User

db.create_all()

db.session.add(User("li", "adiggo@gmail.com", "pass"))

db.session.commit()
