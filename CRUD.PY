from connection import Conexao
import sqlite3

class CRUD():
    def __init__(self):
        self.conexao = Conexao()

    def inserir(self,dados,atributos,entidade):
        #dados é uma lista de valores que sera chamada nas classes que vai precisar adicionar
        sql = f"""INSERT INTO {entidade}({atributos}) VALUES ({dados})"""

        try:
            con = self.conexao.getConexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except sqlite3.Error as er:
            print(er)

entidade = 'TipoLivro'
atributos = 'nomeTipo'
dados = "'Suspense'"
c1 = CRUD()
c1_insert = c1.inserir(dados,atributos,entidade)