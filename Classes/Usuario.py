from Locacao import Locacao

class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._listaLocacoes = []
        self._listaClientes = []

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha

    def set_nome(self, nome):
        self._nome = nome

    def set_email(self, email):
        self._email = email

    def set_senha(self, senha):
        self._senha = senha

    def get_listaLocacoes(self):
        return  self._listaLocacoes
    
    def get_listaClientes(self):
        return  self._listaClientes

    def cadastrar_locacao(self, nomeLocacao, descricaoLocacao, valorLocacao):
        novaLocacao = Locacao(nomeLocacao,descricaoLocacao,valorLocacao)
        self._listaLocacoes.append(novaLocacao)
        
    def cadastrar_cliente(self, nomeCliente, telefoneCliente, cpfCliente):
        novoCliente = Locacao(nomeCliente, telefoneCliente, cpfCliente)
        self._listaClientes.append(novoCliente)

#    def cadastrar_estadia():
#    def alterar_locacao():
#    def alterar_cliente():
#    def alterar_estadia():
#    def deletar_locacao():
#    def deletar_cliente():
#    def deletar_estadia():
#    def pesquisar():