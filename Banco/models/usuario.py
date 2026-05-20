from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Usuario(Model):
    nome = CharField()
    email = CharField()
    senha = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)
    listaClientes = []
    listaLocais = []
    
    class Meta:
        database = db