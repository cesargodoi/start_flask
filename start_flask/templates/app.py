from flask import Flask
{%- if afp %}
from {{ proj }}.ext import site, config, cli{{ ', db, admin, auth' if sqlal else ''}}


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
    
{%- else %}
{%- if sqlal %}
from flask_sqlalchemy import SQLAlchemy
{%- endif %}

app = Flask(__name__)
{%- if sqlal %}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{{ proj }}.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column(
        'email', db.String(100), unique=True, nullable=False
    )
    passwd = db.Column('passwd', db.String)
    admin = db.Column('admin', db.Boolean)

    def __repr__(self):
        return self.email
{%- endif %}

@app.route('/')
def index():
    return 'Hello, {{ proj.upper() }}!'

{%- endif %}