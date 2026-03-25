from Cliente import Cliente
from Usuario import Usuario
from Locacao import Locacao
from Estadia import Estadia

usuarioTeste = Usuario("UsuarioTest", "usuario@mail.com", "001122")

# testes que alteram e retornam atributos
def test_altera_nome():
    usuarioTeste.set_nome("Teste Projeto")
    assert "Teste Projeto" == usuarioTeste.get_nome()

def test_altera_email():
    usuarioTeste.set_email("12_88888-8888")
    assert "12_88888-8888" == usuarioTeste.get_email()

def test_altera_senha():
    usuarioTeste.set_senha("112233")
    assert "112233" == usuarioTeste.get_senha()

# testes de métodos que interagem com outras classes.
def test_criando_nova_locacao():
    usuarioTeste.cadastrar_locacao("Chalé 2", "Chalé com banheira aquecida", 1000)
    assert 1 == len(usuarioTeste.get_listaLocacoes())

def test_cadastrando_novo_cliente():
    usuarioTeste.cadastrar_cliente("Marcio", "3905-2233", "111.111.111-11")
    assert 1 == len(usuarioTeste.get_listaClientes())

def test_cadastrando_nova_estadia():
    usuarioTeste.cadastrar_estadia(Locacao("Quarto em Campos", "Quarto, banheiro amplo, piscina privada aquecida", 1000), Cliente("Jader Teste", "111.111.111-11","(12)99999-9999"), "02/04/2026","10/04/2026")
    assert 1 == len(usuarioTeste.get_listaEstadias())