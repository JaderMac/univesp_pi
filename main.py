from flask import Flask
from routes.home import home_route
from routes.usuario import usuario_route
from routes.cliente import cliente_route
from routes.locacao import locacao_route
from routes.estadia import estadia_route
from routes.relatorio import relatorio_route

Servidor = Flask('ProjetoIntegrador1')
Servidor.json.sort_keys = False

Servidor.register_blueprint(home_route)
Servidor.register_blueprint(usuario_route, url_prefix='/usuario')
Servidor.register_blueprint(cliente_route, url_prefix='/usuario/clientes')
Servidor.register_blueprint(locacao_route, url_prefix='/usuario/locacoes')
Servidor.register_blueprint(estadia_route, url_prefix='/usuario/estadias')
Servidor.register_blueprint(relatorio_route, url_prefix='/usuario/relatorios')

Servidor.run(debug=True)
