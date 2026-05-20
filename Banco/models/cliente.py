from peewee import Model, CharField, DateTimeField, ForeignKeyField
from banco.database import db
from banco.models.usuario import Usuario
import datetime

class Cliente(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    nome = CharField()
    celular = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db