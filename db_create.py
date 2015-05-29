from map_traveller import db
from model import user

db.create_all()

db.session.add(user("li", "adiggo@gmail.com", "pass"))

db.session.commit()
