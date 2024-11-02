
from CRUD import CRUD


class Editora:  
    def __init__(self):
        self.crud = CRUD()
        self.entidade = 'Editora'
        self.atributos = 'nomeEditora'

    def adicionar_editora(self,dados):
        print(dados)
        self.crud.inserir(self.entidade,self.atributos,dados)

    def listar_editora(self):
        return self.crud.listar(self.entidade)
    