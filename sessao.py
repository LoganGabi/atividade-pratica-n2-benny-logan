
from CRUD import CRUD


class Sessao:  
    def __init__(self):
        self.crud = CRUD()
        self.entidade = 'Sessao'
        self.id = None
        self.nomeSessao = 'nomeSessao'
        self.descr = 'descr'
        self.status = 'status'

    def adicionar_Sessao(self,dados):
        atributos = f'"{self.nomeSessao}","{self.descr}","{self.status}"'
        self.crud.inserir(self.entidade,atributos,dados)

    def listar_Sessao(self):
        return self.crud.listar(self.entidade)
    
    def excluir_Sessao(self,id):
        self.crud.excluir(self.entidade,id)
    
    def editar_Sessao(self,id,nome_Sessao,descr,status):
        tupla = f'nomeSessao = "{nome_Sessao}",descr = "{descr}",status = "{status}"'
        self.crud.atualizar(self.entidade,id,tupla)

    # QUANDO FOR SELECIONADO A TUPLA A SER EDITADA, CADA CAMPO VAI SER PEGO ATRAÉS DESSA FUNÇÃO
    def get_dado_Sessao(self,atributo,id):
        return self.crud.get_dado_atributo(self.entidade,atributo,id)
    
    def get_dado(self,atributo):
        return self.crud.get_dado(self.entidade,atributo)