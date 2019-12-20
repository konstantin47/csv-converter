from app import db
from app.models import User


u = User(username='root')
u.set_password('ZEUSrootPASS!')

db.session.add(u)
db.session.commit()
