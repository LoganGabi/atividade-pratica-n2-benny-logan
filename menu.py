import ttkbootstrap as ttk
from ttkbootstrap import Frame
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import tkinter as tk
class TelaLogin:
    def __init__(self, master):
        self.janela = master

        self.menu = ttk.Menu(self.janela, tearoff=0)
        self.mnu_livros = ttk.Menu(self.menu)
        self.mnu_autores = ttk.Menu(self.menu)
        self.mnu_sessoes = ttk.Menu(self.menu)

        self.menu.add_cascade(label='LIVROS', menu=self.mnu_livros,font=12)
        self.menu.add_cascade(label='AUTORES', menu=self.mnu_autores)
        self.menu.add_cascade(label='SESSÕES', menu=self.mnu_sessoes)

        self.mnu_livros.add_command(label='Cadastrar Livro', command=self.cadastrar_livro)
        self.mnu_livros.add_command(label='Visualizar Livro',command=self.exibir_livros)

        self.janela.config(menu=self.menu)

    def cadastrar_livro(self):
        self.top_cadastro_livro = ttk.Toplevel(self.janela)

        self.frm_cad_livro = Frame(self.top_cadastro_livro)
        self.frm_cad_livro.pack(anchor='center', expand=True, side='left')

        self.lbl_nomeLivro = ttk.Label(self.frm_cad_livro, text='Nome')
        self.lbl_nomeLivro.pack()

        #nome, edição, tipo, sessão, autor, editora

    def exibir_livros(self):
        coldata = [
        {"text": "ID", "stretch": False},
        "Nome",
        {"text": "Tipo", "stretch": False},
        {"text": "Sessão", "stretch": False}
        ]

        # rowdata = [
        #     ('A123', 'IzzyCo', 12),
        #     ('A136', 'Kimdee Inc.', 45),
        #     ('A158', 'Farmadding Co.', 36)
        # ]

        trevieww = Tableview(self.janela,coldata=coldata,paginated=True,bootstyle=PRIMARY,height=20)
        trevieww.pack(fill=tk.Y,padx=25,pady=25)
janela = ttk.Window()
janela.resizable(False, False)
# janela.wm_iconposition(10, 10)
janela.geometry("1080x720")
app = TelaLogin(janela)
janela.mainloop()
