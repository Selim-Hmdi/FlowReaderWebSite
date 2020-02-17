from peewee import *
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SqliteDatabase("RSSwebsite.sqlite3")


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel, UserMixin):
    username = CharField()
    password = CharField()


class Flow(BaseModel):
    url = CharField()
    user = ForeignKeyField(User, backref="flows")


def create_tables():
    with db:
        db.create_tables([User, Flow, ])


def drop_tables():
    with db:
        db.drop_tables([User, Flow, ])


def create_user():
    toto = User.create(username="toto", password=generate_password_hash("tutu"))
    thor = User.create(username="thor",password=generate_password_hash("flash"))

        