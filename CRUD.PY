from connection import Conexao
import sqlite3

class CRUD():
    def __init__(self):
        self.conexao = Conexao()

    def inserir(self,entidade,atributos,dados):
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

    def listar(self,entidade):
        sql = f"""SELECT * FROM {entidade}"""
        try:
            con = self.conexao.getConexao()
            cursor = con.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print(f'Este é o resultado {resultado}')
            con.close()
            return resultado
        except sqlite3.Error as er:
            print(er)

entidade = "TipoLivro"
c1 = CRUD()
c1.listar(entidade)
