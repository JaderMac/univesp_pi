from peewee import Model, CharField, DecimalField, DateTimeField, ForeignKeyField
from banco.database import db
import datetime

class Locacao(Model):
    nome = CharField()
    descricao = CharField()
    valorDiaria = DecimalField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db