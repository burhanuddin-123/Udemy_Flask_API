from app import app
from db import db

db.init_app(app)

# create tables
@app.before_first_request
def create_tables():
    db.create_all()

# decorator is shifted from app.py to here due to problem in deployment in heroku    