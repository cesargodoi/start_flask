from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from {{ proj }}.ext.db import db


admin = Admin()
def init_app(app):
    admin.name = '{{ proj.upper() }}'
    admin.template_mode = 'bootstrap3'
    admin.init_app(app)

    # if we have another table to use in the admin,
    # we can do it like this
    # admin.add_view(ModelView(<another_table>, db.session))
