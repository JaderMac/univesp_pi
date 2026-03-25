from Cliente import Cliente
from Locacao import Locacao
from Estadia import Estadia

class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._listaLocacoes = []
        self._listaClientes = []
        self._listaEstadias = []

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
    
    def get_listaEstadias(self):
        return  self._listaEstadias

    def cadastrar_locacao(self, nomeLocacao, descricaoLocacao, valorLocacao):
        novaLocacao = Locacao(nomeLocacao,descricaoLocacao,valorLocacao)
        self._listaLocacoes.append(novaLocacao)
        
    def cadastrar_cliente(self, nomeCliente, telefoneCliente, cpfCliente):
        novoCliente = Locacao(nomeCliente, telefoneCliente, cpfCliente)
        self._listaClientes.append(novoCliente)

    def cadastrar_estadia(self, ClienteEstadia, LocacaoEstadia, dataInicialEstadia, dataFinalEstadia):
        novaEstadia = Estadia(ClienteEstadia, LocacaoEstadia, dataInicialEstadia, dataFinalEstadia)
        self._listaEstadias.append(novaEstadia)
    #
    # pesquisar
    #
    def pesquisar_cliente_por_nome(self, clientePesquisado):
        for cliente in self.get_listaClientes:
            if clientePesquisado.get_nome() == cliente.get_nome():
                return  clientePesquisado
   
    def pesquisar_cliente_por_cpf(self, clientePesquisado):
        for cliente in self.get_listaClientes:
            if clientePesquisado.get_cpf() == cliente.get_cpf():
                return  clientePesquisado
            
    def pesquisar_locacao_por_nome(self, locacaoPesquisada):
        for locacao in self.get_listaLocacoes:
            if locacaoPesquisada.get_nome() == locacao.get_nome():
                return  locacaoPesquisada
                    
    def pesquisar_locacao_por_valor(self, locacaoPesquisada):
        for locacao in self.get_listaLocacoes:
            if locacaoPesquisada.get_valor() == locacao.get_valor():
                return  locacaoPesquisada

    def pesquisar_estadia_por_locacao(self, estadiaPesquisada):
        for estadia in self.get_listaEstadias:
            if estadiaPesquisada.get_locacao() == estadia.get_locacao():
                return  estadiaPesquisada
    
    def pesquisar_estadia_por_dataInicial(self, estadiaPesquisada):
        for estadia in self.get_listaEstadias:
            if estadiaPesquisada.get_dataInicial() == estadia.get_dataInicial():
                return  estadiaPesquisada
    #
    # Alterar cliente
    #
    def alterar_nome_cliente(self, clienteAlterado, novoNomeCliente):
        self.clienteAlterado.set_nome(novoNomeCliente)
    
    def alterar_cpf_cliente(self, clienteAlterado, novoCPFCliente):
        self.clienteAlterado.set_cpf(novoCPFCliente)

    def alterar_telefone_cliente(self, clienteAlterado, novoTelefoneCliente):
        self.clienteAlterado.set_telefone(novoTelefoneCliente)

#    def alterar_cliente():
#    def alterar_estadia():
#    def deletar_locacao():
#    def deletar_cliente():
#    def deletar_estadia():