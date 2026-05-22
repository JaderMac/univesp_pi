from peewee import Model, CharField, DecimalField, DateTimeField, ForeignKeyField
from banco.database import db
from banco.models.usuario import Usuario
import datetime

class Locacao(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    nome = CharField()
    descricao = CharField()
    valorDiaria = DecimalField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db