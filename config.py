from flask import Flask
from routes.home import home_route
from routes.usuario import usuario_route
from routes.cliente import cliente_route
from routes.locacao import locacao_route
from routes.estadia import estadia_route
from routes.relatorio import relatorio_route
from banco.database import db
from banco.models.usuario import Usuario
from banco.models.cliente import Cliente
from banco.models.locacao import Locacao
from banco.models.estadia import Estadia 

def config_all(Servidor):
    config_routes(Servidor)
    config_db()

def config_routes(Servidor):
    Servidor.register_blueprint(home_route)
    Servidor.register_blueprint(usuario_route, url_prefix='/usuario')
    Servidor.register_blueprint(cliente_route, url_prefix='/usuario/clientes')
    Servidor.register_blueprint(locacao_route, url_prefix='/usuario/locacoes')
    Servidor.register_blueprint(estadia_route, url_prefix='/usuario/estadias')
    Servidor.register_blueprint(relatorio_route, url_prefix='/usuario/relatorios')

def config_db():
    db.connect()
    db.create_tables([Usuario, Cliente, Locacao, Estadia])
