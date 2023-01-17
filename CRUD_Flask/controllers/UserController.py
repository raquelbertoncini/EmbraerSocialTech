from flask import Response, request
from models.User import User
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

def index():
    session = db.session()
    users = session.query(User).all()
    users_json = [user.serialize() for user in users]
    session.close()
    return Response(json.dumps(users_json))

def store():
    body = request.get_json()
    session = db.session()

    try:
        user = User(name=body['name'],age=body['age'],address=body['address'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))

    except Exception as e:
        session.rollback()

    finally:
        session.close()
