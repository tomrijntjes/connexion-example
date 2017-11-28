#!/usr/bin/env python3
import os
<<<<<<< HEAD
import datetime
import logging
import connexion
from connexion import NoContent
from pony.orm import *

from models import *


#I don't know yet which hashing strategy we use. This auth class is not secure & just for testing

import hashlib

def hash_pw(raw):
    salted = raw+os.environ["SALT"]
    return hashlib.md5(salted.encode('utf-8')).hexdigest()


    

@db_session
def getUser(email):
    try:
        user = User[email].to_dict()
        return user 
    except ObjectNotFound:
        return ('Not found', 404)

@db_session
def loginUser(email,password):
    logging.info(email)
    logging.info(password)
    validated = User[email].password==hash_pw(password)
    return NoContent, (200 if validated else 403)

@db_session
def logoutUser(email,body):
    return 200


@db_session
def createUser(body):
    User(email=body['email'],nickname=body['nickname'],password=hash_pw(body['password']),creation_date=datetime.utcnow())
    logging.info('Creating user %s..', body['nickname'])
    return NoContent, 200

@db_session
def updateUser(email,body):
    logging.info(user)
    user = User.get(email='email')
    print(user)
    User(name=user['name'],email=email,password=hash_pw(user['password']),created=datetime.utcnow())
    logging.info('Creating user %s..', user_id)
    return NoContent, (200 if exists else 201)

@db_session
def deleteUser(user_id):
    logging.info('Deleting user %s..', user_id)
    Pet[user_id].delete()
    return NoContent, 204
















logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')