from Cliente import Cliente

clienteTeste = Cliente("Jader Teste", "(12)99999-9999","001122" )

# testes que alteram e retornam atributos
def test_altera_nome():
    clienteTeste.set_nome("Teste Projeto")
    assert "Teste Projeto" == clienteTeste.get_nome()

def test_altera_telefone():
    clienteTeste.set_telefone("12_88888-8888")
    assert "12_88888-8888" == clienteTeste.get_telefone()

def test_altera_senha():
    clienteTeste.set_senha("112233")
    assert "112233" == clienteTeste.get_senha()


