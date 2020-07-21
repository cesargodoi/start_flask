from flask import Markup, flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters

from {{ proj }}.ext.auth.models import User
from {{ proj }}.ext.db import db


class UserAdmin(ModelView):
    '''Interface admin de user'''

    def format_user(self, request, user, *args):
        return user.email.split('@')[0]

    column_formatters = {
        'email': format_user
    }

    column_list = ['admin', 'email']

    column_labels = {'email': 'User login'}

    column_searchable_list = ['email']

    column_filters = [
        'email',        'admin',
        filters.FilterLike(
            User.email, 'dominio', options=(
                ('gmail', 'Gmail'), ('uol', 'Uol')
            )
        ),
    ]

    can_edit = False

    can_create = True

    can_delete = True

    # exemple of flask action
    @action('toggle_admin', 'Toggle admin status', 'Are you sure?')
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids))
        for user in users.all():
            user.admin = not user.admin
        db.session.commit()
        flash('Success!', 'success')
        