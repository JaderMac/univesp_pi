class Locacao:
    def __init__(self, nome, descricao, valorDiaria):
        self.nome = nome
        self.descricao = descricao
        self.valorDiaria = valorDiaria

    def get_nome(self):
        return  self.nome

    def get_descricao(self):
        return  self.descricao

    def get_valorDiaria(self):
        return self.valorDiaria

    def set_valorDiaria(self,valorDiaria):
        self.valorDiaria = valorDiaria

    def set_nome(self, nome):
        self.nome = nome

    def set_descricao(self, descricao):
        self.descricao = descricao

