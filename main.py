from flask import Flask
from routes.home import home_route
from routes.usuario import usuario_route
from routes.cliente import cliente_route
from routes.locacao import locacao_route

Servidor = Flask('ProjetoIntegrador1')
Servidor.json.sort_keys = False

Servidor.register_blueprint(home_route)
Servidor.register_blueprint(usuario_route, url_prefix='/usuario')
Servidor.register_blueprint(cliente_route, url_prefix='/usuario/clientes')
Servidor.register_blueprint(locacao_route, url_prefix='/usuario/locacoes')

Servidor.run(debug=True)
