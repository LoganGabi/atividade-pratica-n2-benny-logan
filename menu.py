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
        self.top_cadastro_livro = tk.Toplevel(self.janela,width=100)
        

        # def atualizar_label(janela):
            # if combobox.get()=="Novo Autor":
            #     nvoLivro = ttk.Label(janela,text='Digite o novo autor')
            #     nvoLivro.pack()
            #     cmpNvoLivro = ttk.Entry(janela)
            #     cmpNvoLivro.pack()
        
        
        self.lbl_nomeLivro = ttk.Label(self.top_cadastro_livro, text='Nome')
        self.lbl_nomeLivro.pack()

        self.cmp_nomeLivro = ttk.Entry(self.top_cadastro_livro,width=50)
        self.cmp_nomeLivro.pack(pady=20,padx=40)

        self.lbl_autorLivro = ttk.Label(self.top_cadastro_livro,text='Autor')
        self.lbl_autorLivro.pack()
        self.opcoes = ["Novo Autor", "Opção 2", "Opção 3", "Opção 4"]

        self.combobox_autorLivro = ttk.Combobox(self.top_cadastro_livro, values=self.opcoes,width=50)
        self.combobox_autorLivro.pack(pady=20,padx=40)
        # combobox.bind("<<ComboboxSelected>>", atualizar_label(self.top_cadastro_livro))
        
        self.lbl_nmeEditora = ttk.Label(self.top_cadastro_livro,text='Editora')
        self.lbl_nmeEditora.place(x=200,y=270)

        self.lbl_sessao = ttk.Label(self.top_cadastro_livro,text='Número da Sessão')
        self.lbl_sessao.place(x=40,y=270)

        self.cmp_nmeEditora = ttk.Entry(self.top_cadastro_livro)
        self.cmp_nmeEditora.pack(pady=20,padx=40,side=ttk.LEFT)

        self.opcoesSessao = [1,2,3,4,5,6,7]

        self.combobox_lblSessao = ttk.Combobox(self.top_cadastro_livro,values=self.opcoesSessao,width=25)
        self.combobox_lblSessao.pack(side=ttk.RIGHT)



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
