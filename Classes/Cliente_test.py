from Cliente import Cliente

clienteTeste = Cliente("Jader Teste", "111.111.111-11","(12)99999-9999" )

# testes que alteram e retornam atributos
def test_altera_nome():
    clienteTeste.set_nome("Teste Projeto")
    assert "Teste Projeto" == clienteTeste.get_nome()

def test_altera_telefone():
    clienteTeste.set_telefone("12_88888-8888")
    assert "12_88888-8888" == clienteTeste.get_telefone()

def test_altera_cpf():
    clienteTeste.set_cpf("222.222.222-22")
    assert "222.222.222-22" == clienteTeste.get_cpf()


