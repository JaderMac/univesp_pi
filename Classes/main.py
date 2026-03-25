from Cliente import Cliente
from Usuario import Usuario
from Locacao import Locacao
from Estadia import Estadia

clienteTeste = Cliente("Jader Teste", "111.111.111-11","(12)99999-9999")
locacaoTeste = Locacao("Quarto em Campos", "Quarto, banheiro amplo, piscina privada aquecida", 1000)
estadiaTeste = Estadia(locacaoTeste, clienteTeste, "27/12/2026", "03/01/2027")
usuarioTeste = Usuario("SUPER", "SUPER@USER.COM", "001122")

usuarioTeste.cadastrar_locacao("Chalé 1", "Chalé com banheira aquecida", 1000)
usuarioTeste.cadastrar_locacao("Chalé 2", "Chalé com banheira aquecida", 1000)

# usuarioTeste.cadastrar_estadia(locacaoTeste, clienteTeste,"02/04/2026","10/04/2026")

print(usuarioTeste.cadastrar_estadia(locacaoTeste, clienteTeste,"02/04/2026","10/04/2026"))

# print(estadiaTeste.Locacao.nome)
# print(estadiaTeste.dataInicial)
# print(estadiaTeste.dataFinal)