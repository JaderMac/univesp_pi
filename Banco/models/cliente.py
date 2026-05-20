from peewee import Model, CharField, DateTimeField, ForeignKeyField
from database.database import db
import datetime

class Cliente(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    nome = CharField()
    celular = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db