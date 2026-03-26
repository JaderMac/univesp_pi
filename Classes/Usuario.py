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
        return novaLocacao
        
    def cadastrar_cliente(self, nomeCliente, telefoneCliente, cpfCliente):
        novoCliente = Cliente(nomeCliente, telefoneCliente, cpfCliente)
        self._listaClientes.append(novoCliente)
        return novoCliente

    def cadastrar_estadia(self, ClienteEstadia, LocacaoEstadia, dataInicialEstadia, dataFinalEstadia):
        novaEstadia = Estadia(ClienteEstadia, LocacaoEstadia, dataInicialEstadia, dataFinalEstadia)
        self._listaEstadias.append(novaEstadia)
        return novaEstadia
    #
    # pesquisar
    #
    def pesquisar_cliente_por_nome(self, clientePesquisado):
        for cliente in self.get_listaClientes():
            if clientePesquisado.get_nome().lower() == cliente.get_nome().lower():
                return  clientePesquisado
   
    def pesquisar_cliente_por_cpf(self, clientePesquisado):
        for cliente in self.get_listaClientes():
            if clientePesquisado.get_cpf() == cliente.get_cpf():
                return  clientePesquisado
            
    def pesquisar_locacao_por_nome(self, locacaoPesquisada):
        for locacao in self.get_listaLocacoes():
            if locacaoPesquisada.get_nome() == locacao.get_nome():
                return  locacaoPesquisada
                    
    def pesquisar_locacao_por_valor(self, valorLocacaoPesquisada):
        listaLocacoesPesquisadas = []
        for locacao in self.get_listaLocacoes():
            if valorLocacaoPesquisada == locacao.get_valorDiaria():
                listaLocacoesPesquisadas.append(locacao)
        return listaLocacoesPesquisadas

    def pesquisar_estadia_por_locacao(self, estadiaPesquisada):
        for estadia in self.get_listaEstadias():
            if estadiaPesquisada.get_Locacao() == estadia.get_Locacao():
                return  estadiaPesquisada
    
    def pesquisar_estadia_por_dataInicial(self, estadiaPesquisada):
        for estadia in self.get_listaEstadias():
            if estadiaPesquisada.get_dataInicial() == estadia.get_dataInicial():
                return  estadiaPesquisada
    #
    # Alterar cliente
    #
    def alterar_nome_cliente(self, clienteAlterado, novoNomeCliente):
        return clienteAlterado.set_nome(novoNomeCliente)

    def alterar_cpf_cliente(self, clienteAlterado, novoCPFCliente):
        return clienteAlterado.set_cpf(novoCPFCliente)

    def alterar_telefone_cliente(self, clienteAlterado, novoTelefoneCliente):
        return clienteAlterado.set_telefone(novoTelefoneCliente)
    # #
    # # Alterar locacao
    # #
    def alterar_nome_locacao(self, locacaoAlterada, novoNome):
        return locacaoAlterada.set_nome(novoNome)
    
    def alterar_descricao_locacao(self, locacaoAlterada, novaDescricao):
        return locacaoAlterada.set_descricao(novaDescricao)
    
    def alterar_valorDiaria_locacao(self, locacaoAlterada, novoValorDiaria):
        return locacaoAlterada.set_valorDiaria(novoValorDiaria)
    # #
    # # Alterar estadia
    # #
    def alterar_cliente_estadia(self, estadiaAlterada, novoCliente):
        return estadiaAlterada.set_Cliente(novoCliente)
    
    def alterar_locacao_estadia(self, estadiaAlterada, novaLocacao):
        return estadiaAlterada.set_Locacao(novaLocacao)

    def alterar_dataInicial_estadia(self, estadiaAlterada, novaDataInicial):
        return estadiaAlterada.set_dataInicial(novaDataInicial) 

    def alterar_dataFinal_estadia(self, estadiaAlterada, novaDataFinal):
        return estadiaAlterada.set_dataFinal(novaDataFinal) 

    def deletar_cliente(self, clienteExcluido):
        if clienteExcluido is not None:
            del clienteExcluido
            return 1

    def deletar_locacao(self, locacaoExcluida):
        if locacaoExcluida is not None:
            del locacaoExcluida
            return 1
 
    def deletar_estadia(self, estadiaExcluida):
        if estadiaExcluida is not None:
            del estadiaExcluida
            return 1