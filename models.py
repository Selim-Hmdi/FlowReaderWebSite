from peewee import *
from flask_login import UserMixin


db = SqliteDatabase("RSSwebsite.sqlite3")


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel, UserMixin):
    username = CharField()
    password = CharField()


class Flow(BaseModel):
    url = CharField()
    user = ForeignKeyField(User)


def create_tables():
    with db:
        db.create_tables([User, Flow, ])


def drop_tables():
    with db:
        db.drop_tables([User, Flow, ])
