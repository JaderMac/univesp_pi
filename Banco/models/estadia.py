from peewee import Model, CharField, DecimalField, DateTimeField, ForeignKeyField
from banco.database import db
from banco.models.usuario import Usuario
from banco.models.cliente import Cliente
from banco.models.locacao import Locacao
import datetime

class Estadia(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    cliente = ForeignKeyField(Cliente, backref='cliente')
    locacao = ForeignKeyField(Locacao, backref='locacao')
    dataInicial = DateTimeField()
    dataFinal = DateTimeField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db