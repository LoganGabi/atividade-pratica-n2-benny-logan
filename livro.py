from CRUD import CRUD

class Livro:
    def __init__(self):
       self.crud = CRUD()
       self.entidade = 'Livro'
       self.nomeLivro = 'nomeLivro'
       self.idTipoLivro = 'idTipoLivro'
       self.idAutor = 'idAutor'
       self.idEditora = 'idEditora'
       self.nEdicao = 'edicao'
       self.idSessao = 'idSessao'
    def adicionar_livro(self,dados):
        atributos = f'"{self.nomeLivro}","{self.nEdicao}","{self.idAutor}","{self.idTipoLivro}","{self.idEditora}","{self.idSessao}"'
        self.crud.inserir(self.entidade,atributos,dados)
    def listar_livros(self):
        return self.crud.listar(self.entidade)

    def excluir_livro(self,id):
        self.crud.excluir(self.entidade,id)
    
    def editar_livro(self,id,nome_livro,nedicao,idAutor,idTipoLivro,idEditora,idSessao):
        tupla = f'nomeLivro = "{nome_livro}",edicao = "{nedicao}",idAutor = "{idAutor}",idTipoLivro = "{idTipoLivro}", idEditora = "{idEditora}",idSessao = "{idSessao}"'
        self.crud.atualizar(self.entidade,id,tupla)

    # QUANDO FOR SELECIONADO A TUPLA A SER EDITADA, CADA CAMPO VAI SER PEGO ATRAÉS DESSA FUNÇÃO
    def get_dado_livro(self,atributo,id):
        return self.crud.get_dado_atributo(self.entidade,atributo,id)