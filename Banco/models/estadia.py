from peewee import Model, CharField, DecimalField, DateTimeField, ForeignKeyField
from banco.database import db
from banco.models.cliente import Cliente
from banco.models.locacao import Locacao
import datetime

class Estadia(Model):
    cliente = ForeignKeyField(Cliente, backref='cliente')
    locacao = ForeignKeyField(Locacao, backref='locacao')
    dataInicial = DateTimeField()
    dataFinal = DateTimeField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db