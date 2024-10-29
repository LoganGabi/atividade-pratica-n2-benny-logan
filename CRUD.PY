from connection import Conexao


class CRUD():
    def __init__(self):
        self.conexao = Conexao()

    def inserir(self,dados,atributos,entidade):
        #dados é uma lista de valores que sera chamada nas classes que vai precisar adicionar
        sql = f"""INSERT INTO {entidade}({atributos}) """
