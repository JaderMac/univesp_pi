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

def test_pesquisando_estadia_por_locacao():
    estadiaCriada = usuarioTeste.cadastrar_estadia(Locacao("Quarto em Campos","Quarto",1000),Cliente("Jader","111.111.111-11","(12)99999"),"02/04/2026","10/04/2026")
    estadiaPesquisada = usuarioTeste.pesquisar_estadia_por_locacao(estadiaCriada)
    assert estadiaCriada == estadiaPesquisada

def test_pesquisando_estadia_por_dataInicial(): 
    estadiaCriada = usuarioTeste.cadastrar_estadia(Locacao("Quarto em Campos","Quarto",1000),Cliente("Jader","111.111.111-11","(12)99999"),"02/04/2026","10/04/2026")
    estadiaPesquisada = usuarioTeste.pesquisar_estadia_por_dataInicial(estadiaCriada)
    assert estadiaCriada == estadiaPesquisada

# testes de alteração
def test_alterando_nome_cliente():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    usuarioTeste.alterar_nome_cliente(novoCliente, "Lucas")
    assert "Lucas" == novoCliente.get_nome()

def test_alterando_cpf_cliente():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    usuarioTeste.alterar_cpf_cliente(novoCliente, "012")
    assert "012" == novoCliente.get_cpf()

def test_alterando_telefone_cliente():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    usuarioTeste.alterar_telefone_cliente(novoCliente, "123")
    assert "123" == novoCliente.get_telefone()

def test_alterando_nome_locacao():
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    usuarioTeste.alterar_nome_locacao(novaLocacao,"Quarto 1")
    assert "Quarto 1" == novaLocacao.get_nome()

def test_alterando_descricao_locacao():
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    usuarioTeste.alterar_descricao_locacao(novaLocacao,"quarto com varanda")
    assert "quarto com varanda" == novaLocacao.get_descricao()

def test_alterando_valorDiaria_locacao():
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    usuarioTeste.alterar_valorDiaria_locacao(novaLocacao,800)
    assert 800 == novaLocacao.get_valorDiaria()

def test_alterando_cliente_estadia():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    novoCliente2 = usuarioTeste.cadastrar_cliente("Amanda Teste", "129888888", "111.111.111-11")
    novaEstadia = usuarioTeste.cadastrar_estadia("Chalé 1", "Quarto com varanda", "25/01/27", "29/01/21")
    usuarioTeste.alterar_cliente_estadia(novaEstadia, novoCliente2)
    assert novoCliente2.get_nome() == novaEstadia.get_Cliente().get_nome()

def test_alterando_locacao_estadia():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    novaLocacao0 = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    novaLocacao1 = usuarioTeste.cadastrar_locacao("Chalé 2", "Chalé com banheira aquecida", 1000)
    novaEstadia = usuarioTeste.cadastrar_estadia(novaLocacao0 , novoCliente,"02/04/2026","10/04/2026")
    usuarioTeste.alterar_locacao_estadia(novaEstadia, novaLocacao1)
    assert "Chalé 2" == novaEstadia.get_Locacao().get_nome()

def test_alterando_dataInicial_estadia():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    novaEstadia = usuarioTeste.cadastrar_estadia(novaLocacao , novoCliente,"02/04/2026","10/04/2026")
    usuarioTeste.alterar_dataInicial_estadia(novaEstadia, "22/12/2027")
    assert  "22/12/2027" == novaEstadia.get_dataInicial()

def test_alterando_dataFinal_estadia():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    novaEstadia = usuarioTeste.cadastrar_estadia(novaLocacao , novoCliente,"02/04/2026","10/04/2026")
    usuarioTeste.alterar_dataFinal_estadia(novaEstadia, "31/12/2027")
    assert  "31/12/2027" == novaEstadia.get_dataFinal()

def test_excluir_cliente():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    assert 1 == usuarioTeste.deletar_cliente(novoCliente)

def test_excluir_locacao():
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    assert 1 == usuarioTeste.deletar_locacao(novaLocacao)

def test_excluir_estadia():
    novoCliente = usuarioTeste.cadastrar_cliente("Jader Teste", "129888888", "111.111.111-11")
    novaLocacao = usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
    novaEstadia = usuarioTeste.cadastrar_estadia(novaLocacao , novoCliente,"02/04/2026","10/04/2026")
    assert 1 == usuarioTeste.deletar_estadia(novaEstadia)
