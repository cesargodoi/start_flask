from flask_migrate import Migrate

from {{ proj }}.ext.db import db
from {{ proj }}.ext.auth import models  # noqa
# import all the project models here

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
