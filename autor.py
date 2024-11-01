
from CRUD import CRUD


class Autor:  
    def __init__(self):
        self.crud = CRUD()
        self.entidade = 'Autor'
        self.atributos = 'nomeAutor'

    def adicionar_autor(self,dados):
        return self.crud.inserir(self.entidade,self.atributos,dados)

    def listar_autor(self):
        return self.crud.listar(self.entidade)
    


