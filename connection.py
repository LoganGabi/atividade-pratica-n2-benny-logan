import sqlite3


class Conexao:
    def getConexao(self):
        caminho = "./bancoBiblio.db"
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
            print('Conectou!')
        except sqlite3.Error as er:
            print(er)
        return conexao
    

