from flask import Flask
from {{ proj }}.ext import site, config, cli {{ ', db, admin, auth' if sqlal else ''}}


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    {%- if sqlal %}
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    {%- endif %}
    
    # here we invoke each extension's init_app function
    
    cli.init_app(app)
    site.init_app(app)
    return app
