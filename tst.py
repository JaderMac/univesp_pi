from banco.database import db
from  banco.models.usuario import Usuario

Usuario.create(nome="Jader Teste", email="jader0@univesp.pi", senha="112233")