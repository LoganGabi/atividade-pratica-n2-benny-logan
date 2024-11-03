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
        ...