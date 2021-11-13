import os
import re

from flask import Flask
from flask.templating import render_template
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity # 2 function of security.py
from resources.user import UserRegister
from resources.item import Items,Item
from resources.store import Store, StoreList

app = Flask(__name__)

# fetch connection strings
uri = os.environ.get('DATABASE_URL', 'sqlite:///new_data.db')  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

# configuration of SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'jose'
api = Api(app)


# app.config['JWT_AUTH_URL_RULE'] = '/login'  # will change the url from /auth to /login, as by default it is /auth
jwt = JWT(app, authenticate, identity)

# api.add_resource(Index, '/')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)