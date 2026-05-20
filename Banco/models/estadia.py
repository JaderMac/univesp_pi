from peewee import Model, CharField, DecimalField, DateTimeField, ForeignKeyField
from database.database import db
import datetime

class Estadia(Model):
    cliente = ForeignKeyField(Cliente, backref='cliente')
    locacao = ForeignKeyField(Locacao, backref='locacao')
    dataInicial = DateTimeField()
    dataFinal = DateTimeField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db