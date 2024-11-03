
from CRUD import CRUD


class Editora:  
    def __init__(self):
        self.crud = CRUD()
        self.entidade = 'Editora'
        self.id = None
        self.nomeEditora = 'nomeEditora'

    def adicionar_editora(self,dados):
        print(dados)
        self.crud.inserir(self.entidade,self.nomeEditora,dados)

    def listar_editora(self):
        return self.crud.listar(self.entidade)
    
    def excluir_editora(self,id):
        self.crud.excluir(self.entidade,id)
    
    def editar_editora(self,id,nome_editora):
        tupla = f'nomeEditora = "{nome_editora}"'
        self.crud.atualizar(self.entidade,id,tupla)

    # QUANDO FOR SELECIONADO A TUPLA A SER EDITADA, CADA CAMPO VAI SER PEGO ATRAÉS DESSA FUNÇÃO
    def get_dado_editora(self,atributo,id):
        return self.crud.get_dado_atributo(self.entidade,atributo,id)
    
    def get_dado(self,atributo):
        return self.crud.get_dado(self.entidade,atributo)
    