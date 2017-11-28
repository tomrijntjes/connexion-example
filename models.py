import os

from datetime import datetime
from pony.orm import *


db = Database(provider='mysql', user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'], host='artis_users-db_1', database=os.environ['MYSQL_DATABASE'])
set_sql_debug(True)

class User(db.Entity):
    email = PrimaryKey(str)
    password = Required(str)
    nickname = Required(str)
    status = Optional(bool)
    creation_date = Required(datetime)
    last_login = Optional(datetime)
    last_acces_page = Optional(str)



db.generate_mapping()