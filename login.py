import ttkbootstrap as ttk
from ttkbootstrap import Frame
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import tkinter as tk
from autor import Autor
class TelaLogin:
    def __init__(self, master):
        self.janela = master

        self.autor = Autor()
# ----------------TELA DE LOGIN ----------------------------
        self.frmL = ttk.Frame(self.janela, style='danger')
        self.frmL.pack(anchor='center', expand=True, side='left')

        self.lbl1 = ttk.Label(self.frmL, text='Bem-vindo à Biblioteca')
        self.lbl1.pack(anchor='nw')

        self.frmR = ttk.Frame(self.janela)
        self.frmR.pack(anchor='center', expand=True, side='left')

        self.lbl2 = ttk.Label(self.frmR, text='Login')
        self.lbl2.pack(anchor='nw', pady=50)

        self.lblUser = ttk.Label(self.frmR, text='Usuário:')
        self.lblUser.pack(anchor='w')
        self.entUser = ttk.Entry(self.frmR)
        self.entUser.pack()

        self.lblSenha = ttk.Label(self.frmR, text='Senha:')
        self.lblSenha.pack(anchor='w')
        self.entSenha = ttk.Entry(self.frmR)
        self.entSenha.pack()

        self.btnEntrar = ttk.Button(text='ENTRAR',command=self.entrar_sistema)
        self.btnEntrar.pack()
# ----------------TELA DE LOGIN ----------------------------

# ----------------TREVIEWW LIVRO ----------------------------
        self.coldataLivro = [
        {"text": "ID", "stretch": False},
        "Nome",
        {"text": "Tipo", "stretch": False},
        {"text": "Sessão", "stretch": False}
        ]
        self.trevieewLivro = Tableview(self.janela,coldata=self.coldataLivro,paginated=True,bootstyle=PRIMARY,height=20)
# ----------------TREVIEEW LIVRO ----------------------------

# ----------------TREVIEEW AUTOR ----------------------------
        self.coldataAutor =  [
        {"text": "ID", "stretch": False},
        "Nome",
        {"text": "nomeAutor", "stretch": False}
        ]

        self.trevieewAutor = Tableview(self.janela,coldata=self.coldataAutor,paginated=True,bootstyle=PRIMARY,height=20)
# ----------------TREVIEWW AUTOR ----------------------------
    
    def entrar_sistema(self):
        self.frmL.destroy()
        self.lbl1.destroy()
        self.frmR.destroy()
        self.lbl2.destroy()
        self.lblUser.destroy()
        self.entUser.destroy()
        self.lblSenha.destroy()
        self.entSenha.destroy()
        self.btnEntrar.destroy()

        self.menu = ttk.Menu(self.janela, tearoff=0)
        self.mnu_livros = ttk.Menu(self.menu)
        self.mnu_autores = ttk.Menu(self.menu)
        self.mnu_sessoes = ttk.Menu(self.menu)

        self.menu.add_cascade(label='LIVROS', menu=self.mnu_livros,font=12)
        self.menu.add_cascade(label='AUTORES', menu=self.mnu_autores)
        self.menu.add_cascade(label='SESSÕES', menu=self.mnu_sessoes)

        self.mnu_livros.add_command(label='Cadastrar Livro', command=self.cadastrar_livro)
        self.mnu_livros.add_command(label='Visualizar Livro',command=self.exibir_livros)

        self.mnu_autores.add_command(label='Cadastrar Autor',command=None)
        self.mnu_autores.add_command(label='Visualizar Autores',command=self.exibir_autores)

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
        
        self.lbl_nmeEditora = ttk.Label(self.top_cadastro_livro,text='Editora')
        self.lbl_nmeEditora.pack(anchor='w',padx=40)

        self.lbl_sessao = ttk.Label(self.top_cadastro_livro,text='Número da Sessão')
        self.lbl_sessao.pack(anchor='e',padx=40)

        self.opcoesSessao = [1,2,3,4,5,6,7]

        self.cmp_nmeEditora = ttk.Combobox(self.top_cadastro_livro,values=self.opcoesSessao,width=25)
        self.cmp_nmeEditora.pack(side=ttk.LEFT,anchor='w',pady=30,padx=20)

        self.combobox_lblSessao = ttk.Combobox(self.top_cadastro_livro,values=self.opcoesSessao,width=25)
        self.combobox_lblSessao.pack(side=ttk.RIGHT,anchor='e',pady=30,padx=20)

        #nome, edição, tipo, sessão, autor, editora

    def exibir_livros(self):
        self.trevieewAutor.destroy()
        self.trevieewLivro.destroy()
        self.coldataLivro = [
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

        self.trevieewLivro = Tableview(self.janela,coldata=self.coldataLivro,paginated=True,bootstyle=PRIMARY,height=20)
        self.trevieewLivro.pack(fill=tk.Y,padx=25,pady=25)

    def exibir_autores(self):
        self.trevieewLivro.destroy()
        self.trevieewAutor.destroy()

        autorGet = self.autor.listar_autor()
        self.coldataAutor =  [
        {"text": "ID", "stretch": False},
        {"text": "nomeAutor", "stretch": False}
        ]
        self.rowdataAutor = autorGet

        # rowdata = 
        self.trevieewAutor = Tableview(self.janela,coldata=self.coldataAutor,rowdata=self.rowdataAutor,paginated=True,bootstyle=PRIMARY,height=20)
        self.trevieewAutor.pack(fill=tk.Y,padx=25,pady=25)
    




janela = ttk.Window()
janela.resizable(False, False)
janela.wm_iconposition(10, 10)
janela.geometry("1080x720")
app = TelaLogin(janela)
janela.mainloop()
