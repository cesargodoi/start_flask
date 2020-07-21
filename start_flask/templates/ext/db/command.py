from {{ proj }}.ext.auth.models import User
from {{ proj }}.ext.db import db


def create_db():
    '''Creates database'''
    db.create_all()
def drop_db():
    '''Cleans database'''
    db.drop_all()