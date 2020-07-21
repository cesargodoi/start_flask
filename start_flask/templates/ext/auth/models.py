from {{ proj }}.ext.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(100), unique=True, 
nullable=False)
    passwd = db.Column('passwd', db.String)
    admin = db.Column('admin', db.Boolean)

    def __repr__(self):
        return self.email