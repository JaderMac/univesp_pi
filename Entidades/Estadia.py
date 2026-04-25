class Estadia:
    def __init__(self, Locacao, Cliente, dataInicial, dataFinal):
        self.Locacao = Locacao
        self.Cliente = Cliente
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal

    def get_Locacao(self):
        return self.Locacao

    def get_Cliente(self):
        return self.Cliente

    def get_dataInicial(self):
        return self.dataInicial

    def get_dataFinal(self):
        return self.dataFinal

    def set_Locacao(self, Locacao):
        self.Locacao = Locacao

    def set_Cliente(self, Cliente):
        self.Cliente = Cliente

    def set_dataInicial(self, dataInicial):
        self.dataInicial = dataInicial

    def set_dataFinal(self, dataFinal):
        self.dataFinal = dataFinal

