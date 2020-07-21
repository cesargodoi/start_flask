from {{ proj }}.ext.admin import admin as base_admin
from {{ proj }}.ext.auth.admin import UserAdmin
from {{ proj }}.ext.auth.models import User
from {{ proj }}.ext.db import db


def init_app(app):
    '''TODO: init Flask Simple Login + JWT'''
    base_admin.add_view(UserAdmin(User, db.session))
