import ttkbootstrap as ttk
from ttkbootstrap import Frame


class TelaLogin:
    def __init__(self, master):
        self.janela = master

        self.menu = ttk.Menu(self.janela, tearoff=0)
        self.mnu_livros = ttk.Menu(self.menu)
        self.mnu_autores = ttk.Menu(self.menu)
        self.mnu_sessoes = ttk.Menu(self.menu)

        self.menu.add_cascade(label='LIVROS', menu=self.mnu_livros)
        self.menu.add_cascade(label='AUTORES', menu=self.mnu_autores)
        self.menu.add_cascade(label='SESSÕES', menu=self.mnu_sessoes)

        self.mnu_livros.add_command(label='Casdastrar Livro', command=self.cadastrar_livro)
        self.mnu_livros.add_command(label='Vizualizar Livro')

        self.janela.config(menu=self.menu)

    def cadastrar_livro(self):
        self.top_cadastro_livro = ttk.Toplevel(self.janela)

        self.frm_cad_livro = Frame(self.top_cadastro_livro)
        self.frm_cad_livro.pack(anchor='center', expand=True, side='left')

        self.lbl_nomeLivro = ttk.Label(self.frm_cad_livro, text='Nome')
        self.lbl_nomeLivro.pack()

        #nome, edição, tipo, sessão, autor, editora

janela = ttk.Window()
janela.resizable(False, False)
# janela.wm_iconposition(10, 10)
janela.geometry("1080x720")
app = TelaLogin(janela)
janela.mainloop()
