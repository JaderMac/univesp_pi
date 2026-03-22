from Locacao import Locacao

locacaoTeste = Locacao("Quarto em Campos", "Quarto, banheiro amplo, piscina privada aquecida", 1000)

# testes que alteram e retornam atributos
def test_altera_nome():
    locacaoTeste.set_nome("Chalé 1")
    assert "Teste Projeto" == locacaoTeste.get_nome()

def test_altera_descricao():
    locacaoTeste.set_descricao("12_88888-8888")
    assert "12_88888-8888" == locacaoTeste.get_descricao()

def test_altera_valorDiaria():
    locacaoTeste.set_valorDiaria(1500)
    assert 1500 == locacaoTeste.get_valorDiaria()