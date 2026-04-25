from Cliente import Cliente
from Locacao import Locacao
from Estadia import Estadia

clienteTeste = Cliente("Jader Teste", "111.111.111-11","(12)99999-9999")
clienteTeste2 = Cliente("Jader Teste 2", "222.222.222-22","(11)88888-8888")
locacaoTeste = Locacao("Quarto em Campos", "Quarto, banheiro amplo, piscina privada aquecida", 1000)
locacaoTeste2 = Locacao("Quarto em Campos 2", "2 - Quarto, banheiro amplo, piscina privada aquecida", 2000)

estadiaTeste = Estadia(locacaoTeste, clienteTeste, "27/12/2026", "03/01/2027")

def test_altera_locacao():
    estadiaTeste.set_Locacao(locacaoTeste2)
    assert "Quarto em Campos 2" == estadiaTeste.get_Locacao().get_nome()

def test_altera_cliente():
    estadiaTeste.set_Cliente(clienteTeste2)
    assert "Jader Teste 2" == estadiaTeste.get_Cliente().get_nome()

def test_altera_dataInicial():
    estadiaTeste.set_dataInicial("10/10/2027")
    assert "10/10/2027" == estadiaTeste.get_dataInicial()

def test_altera_dataFinal():
    estadiaTeste.set_dataFinal("15/10/2027")
    assert "15/10/2027" == estadiaTeste.get_dataFinal()
