
from CRUD import CRUD


class TipoLivro:  
    def __init__(self):
        self.crud = CRUD()
        self.entidade = 'TipoLivro'
        self.nomeTipoLivro = 'nomeTipo'

    def adicionar_TipoLivro(self,dados):
        atributos = f'"{self.nomeTipoLivro}"'
        self.crud.inserir(self.entidade,atributos,dados)

    def get_dado_TipoLivro(self,atributo,id):
        return self.crud.get_dado_atributo(self.entidade,atributo,id)
    
    def get_dado(self,atributo):
        return self.crud.get_dado_cad(self.entidade,atributo)
    

  