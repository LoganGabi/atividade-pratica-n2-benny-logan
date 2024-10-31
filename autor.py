
from CRUD import CRUD


class Autor:  
    def __init__(self):
        self.crud = CRUD
        self.entidade = 'Autor'
        self.atributos = 'nomeAutor'

    def adicionar_autor(self,dados):
        self.crud = CRUD()
        self.crud.inserir(self.entidade,self.atributos,dados)

    def listar_autor(self):
        self.crud.listar(self.entidade)
    

a1 = Autor()
dado = "'J.K Rowling'"
a1_add = a1.adicionar_autor(dado)
