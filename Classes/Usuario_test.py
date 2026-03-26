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

# testes de métodos que interagem com outras classes Criação.
def test_cadastrando_nova_locacao():
    usuarioTeste.cadastrar_locacao("Chalé 2", "Chalé com banheira aquecida", 1000)
    assert 1 == len(usuarioTeste.get_listaLocacoes())

def test_cadastrando_novo_cliente():
    usuarioTeste.cadastrar_cliente("Marcio", "3905-2233", "111.111.111-11")
    assert 1 == len(usuarioTeste.get_listaClientes())

def test_cadastrando_nova_estadia():
    usuarioTeste.cadastrar_estadia(Locacao("Quarto em Campos", "Quarto, banheiro amplo, piscina privada aquecida", 1000), Cliente("Jader Teste", "111.111.111-11","(12)99999-9999"), "02/04/2026","10/04/2026")
    assert 1 == len(usuarioTeste.get_listaEstadias())

# testes de métodos de pesquisa
def test_pesquisando_cliente_por_nome():
    clienteCriado = usuarioTeste.cadastrar_cliente("Marcio", "111.111.111-11", "3905-2233")
    clientePesquisado = usuarioTeste.pesquisar_cliente_por_nome(clienteCriado)
    assert  "Marcio" == clientePesquisado.get_nome()

def test_pesquisando_cliente_por_cpf():
    clienteCriado = usuarioTeste.cadastrar_cliente("Marcio", "111.111.111-11", "3905-2233")
    clientePesquisado = usuarioTeste.pesquisar_cliente_por_cpf(clienteCriado)
    assert  "111.111.111-11" == clientePesquisado.get_cpf()

def test_pesquisando_locacao_por_nome():
    locacaoCriada = usuarioTeste.cadastrar_locacao("Quarto em Campos", "Quarto com banheiro", 1000)
    locacaoPesquisada = usuarioTeste.pesquisar_locacao_por_nome(locacaoCriada)
    assert "Quarto em Campos" == locacaoPesquisada.get_nome()

def test_pesquisando_locacao_por_valor_uma_locacao():
    locacaoCriada = usuarioTeste.cadastrar_locacao("Quarto em Campos", "Quarto com banheiro", 100)
    listaLocacoesPesquisada = usuarioTeste.pesquisar_locacao_por_valor(100)
    assert 1 == len(listaLocacoesPesquisada)

def test_pesquisando_locacao_por_valor_varias_locacoes():
    locacaoCriada1 = usuarioTeste.cadastrar_locacao("Quarto em Campos", "Quarto com banheiro", 100)
    locacaoCriada2 = usuarioTeste.cadastrar_locacao("Quarto em Campos 2 ", "Quarto com banheiro", 150)
    locacaoCriada3 = usuarioTeste.cadastrar_locacao("Quarto em Campos 3 ", "Quarto com banheiro", 100)
    locacaoCriada4 = usuarioTeste.cadastrar_locacao("Quarto em Campos 4 ", "Quarto com banheiro", 150)
    listaLocacoesPesquisada = usuarioTeste.pesquisar_locacao_por_valor(150)
    assert 2 == len(listaLocacoesPesquisada)