
from CRUD import CRUD


class Autor:  
    def __init__(self):
        self.crud = CRUD()
        self.entidade = 'Autor'
        self.id = None
        self.atributos = 'nomeAutor'

    def adicionar_autor(self,dados):
        print(dados)
        self.crud.inserir(self.entidade,self.atributos,dados)

    def listar_autor(self):
        return self.crud.listar(self.entidade)
    
    def excluir_autor(self,id):
        self.crud.excluir(self.entidade,id)
    
    def editar_autor(self,id,nome_autor):
        tupla = f'nomeAutor = "{nome_autor}"'
        self.crud.atualizar(self.entidade,id,tupla)

    # QUANDO FOR SELECIONADO A TUPLA A SER EDITADA, CADA CAMPO VAI SER PEGO ATRAÉS DESSA FUNÇÃO
    def get_dado_autor(self,atributo,id):
        return self.crud.get_dado_atributo(self.entidade,atributo,id)
    
