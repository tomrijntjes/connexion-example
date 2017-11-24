#!/usr/bin/env python3
import os
import connexion
from pony.orm import *

import datetime
import logging

from connexion import NoContent

db = Database(provider='postgres', user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'], host='connexionexample_pets-db_1', database='')


class Pet(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    created = Optional(datetime.datetime)
    animal_type = Required(str)

db.generate_mapping(create_tables=True)


@db_session
def get_pets(limit, animal_type=None):
    pets = select(p for p in Pet)
    return [pet.to_dict() for pet in pets]

@db_session
def get_pet(pet_id):
    try:
        pet = Pet[pet_id].to_dict()
        return pet 
    except ObjectNotFound:
        return ('Not found', 404)

@db_session
def put_pet(pet_id, pet):
    logging.info(pet_id)
    logging.info(pet)
    if exists:
        logging.info('Updating pet %s..', pet_id)
        Pet(id=pet_id,name=pet['name'],animal_type=pet['animal_type'])
    else:
        logging.info('Creating pet %s..', pet_id)
        Pet(id=pet_id,name=pet['name'],animal_type=pet['animal_type'], created=datetime.datetime.utcnow())
    return NoContent, (200 if exists else 201)

@db_session
def delete_pet(pet_id):
    logging.info('Deleting pet %s..', pet_id)
    Pet[pet_id].delete()
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