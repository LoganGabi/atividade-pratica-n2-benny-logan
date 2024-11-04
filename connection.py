import os
import sqlite3
import sys
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

class Conexao:
    def getConexao(self):
        caminho = resource_path("bancoBiblio.db")
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
            print('Conectou!')
        except sqlite3.Error as er:
            print(er)
        return conexao
    

