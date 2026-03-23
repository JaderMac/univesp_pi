from Usuario import Usuario

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