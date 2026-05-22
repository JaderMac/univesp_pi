from flask import Flask
from config import config_all

Servidor = Flask('ProjetoIntegrador1')
Servidor.json.sort_keys = False

config_all(Servidor)

Servidor.run(debug=True)