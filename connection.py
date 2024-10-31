import sqlite3


class Conexao:
    def createConexao(self):
        caminho = "./bancoBiblio.sqbpro"
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
            print('Conectou!')
        except sqlite3.Error as er:
            print(er)
        return conexao
    
c = Conexao().createConexao()
