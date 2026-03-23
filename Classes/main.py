from Cliente import Cliente
from Usuario import Usuario
from Locacao import Locacao
from Estadia import Estadia

clienteTeste = Cliente("Jader Teste", "111.111.111-11","(12)99999-9999")
locacaoTeste = Locacao("Quarto em Campos", "Quarto, banheiro amplo, piscina privada aquecida", 1000)
estadiaTeste = Estadia(locacaoTeste, clienteTeste, "27/12/2026", "03/01/2027")

print(estadiaTeste.Cliente.nome)
print(estadiaTeste.Locacao.nome)
print(estadiaTeste.dataInicial)
print(estadiaTeste.dataFinal)