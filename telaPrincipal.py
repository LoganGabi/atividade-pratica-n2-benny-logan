import ttkbootstrap as ttk
from ttkbootstrap import Frame, Label, Entry, Button, Combobox
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import tkinter as tk
from autor import Autor
from editora import Editora
from ttkbootstrap.dialogs import Messagebox
import sys
import os

from livro import Livro
from sessao import Sessao
from tipoLivro import TipoLivro

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

class TelaLogin:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Biblioteca Pessoal')

        # alteração do ícone da janela
        caminho_logo = resource_path("logo_biblio.png")
        self.icone = tk.PhotoImage(file=caminho_logo)
        self.janela.wm_iconphoto(False, self.icone)

        # fontes padrão
        self.fontelbl = ttk.font.Font(size=12, weight='bold')
        self.fonteent = ttk.font.Font(size=12, weight='normal')

        self.autor = Autor()
# ----------------TELA DE LOGIN ----------------------------
        self.frmLoginL = Frame(self.janela)
        self.frmLoginL.pack(anchor='center', expand=True, side='left')

        self.imgLogo = ttk.Label(self.frmLoginL, image=self.icone)
        self.imgLogo.pack()

        self.lbl1 = Label(self.frmLoginL, text='Bem-vindo à Biblioteca', font=self.fontelbl)
        self.lbl1.pack()

        self.frmLoginR = Frame(self.janela)
        self.frmLoginR.pack(anchor='center', expand=True, side='left')

        self.lbl2 = Label(self.frmLoginR, text='Login', font=self.fontelbl)
        self.lbl2.pack(anchor='nw', pady=50)

        self.lblUser = Label(self.frmLoginR, text='Usuário:', font=self.fontelbl)
        self.lblUser.pack(anchor='w')
        self.entUser = Entry(self.frmLoginR, font=self.fonteent)
        self.entUser.pack(pady=5)

        self.lblSenha = Label(self.frmLoginR, text='Senha:', font=self.fontelbl)
        self.lblSenha.pack(anchor='w')
        self.entSenha = Entry(self.frmLoginR, font=self.fonteent, show='*')
        self.entSenha.pack(pady=5)

        self.btnEntrar = Button(self.frmLoginR, text='ENTRAR',command=self.confirmacaoLogin)
        self.btnEntrar.pack(pady=10)

    def confirmacaoLogin(self):
        if self.entUser.get() == 'adm' and self.entSenha.get() == 'adm':
            self.entrar_sistema()
        else:
            Messagebox.show_warning('Verifique suas informações de login.','Credenciais incorretas')

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
        {"text": "nomeAutor", "stretch": False}
        ]

        self.trevieewAutor = Tableview(self.janela,coldata=self.coldataAutor,paginated=True,bootstyle=PRIMARY,height=20)
# ----------------TREVIEEW AUTOR ----------------------------

# ----------------TREVIEEW SESSÃO ----------------------------
        self.coldataSessao = [
            {"text":"ID","stretch":False},
            {"text":"numeroSessao","stretch":False}
        ]

        self.trevieewSessao = Tableview(self.janela,coldata=self.coldataSessao,paginated=True,bootstyle=PRIMARY,height=20)
# ----------------TREVIEEW SESSÃO ----------------------------

# ----------------TREVIEEW EDITORA ----------------------------
        self.coldataEditora = [
            {"text":"ID","stretch":False},
            {"text":"nomeEditora","stretch":False}
        ]

        self.trevieewEditora = Tableview(self.janela,coldata=self.coldataEditora,paginated=True,bootstyle=PRIMARY,height=20)
        self.frame_botoesEditoras = tk.Frame(self.janela)
# ----------------TREVIEEW EDITORA ----------------------------
    
    def entrar_sistema(self):
        # destruição dos frames de login ao entrar no sistema
        self.frmLoginL.destroy()
        self.frmLoginR.destroy()

        # configurações Menu
        self.menu = ttk.Menu(self.janela, tearoff=0)
        self.mnu_livros = ttk.Menu(self.menu)
        self.mnu_autores = ttk.Menu(self.menu)
        self.mnu_sessoes = ttk.Menu(self.menu)
        self.mnu_editoras = ttk.Menu(self.menu)
        self.mnu_temas = ttk.Menu(self.menu)

        self.menu.add_cascade(label='LIVROS', menu=self.mnu_livros, font=self.fontelbl)
        self.menu.add_cascade(label='AUTORES', menu=self.mnu_autores)
        self.menu.add_cascade(label='SESSÕES', menu=self.mnu_sessoes)
        self.menu.add_cascade(label="EDITORAS",menu=self.mnu_editoras)
        self.menu.add_cascade(label="TEMAS", menu=self.mnu_temas)

        self.mnu_livros.add_command(label='Cadastrar Livro', command=self.cadastrar_livro)
        self.mnu_livros.add_command(label='Visualizar Livro',command=self.exibir_livros)

        self.mnu_autores.add_command(label='Cadastrar Autor',command=self.cadastrar_autor)
        self.mnu_autores.add_command(label='Visualizar Autores',command=self.exibir_autores)

        self.mnu_sessoes.add_command(label='Cadastrar Sessão',command=self.cadastrar_sessao)
        self.mnu_sessoes.add_command(label='Visualizar Sessão',command=self.exibir_sessoes)

        self.mnu_editoras.add_command(label="Cadastrar Editora",command=self.cadastrar_editora)
        self.mnu_editoras.add_command(label="Visualizar Editora",command=self.exibir_editoras)

        self.mnu_temas.add_command(label="Alterar Tema", command=self.alterar_tema)

        self.janela.config(menu=self.menu)



        # RESOLVE O BUG DOS BOTOES
        self.frame_botoesAutores = tk.Frame(self.janela)
        self.frame_botoesEditoras = tk.Frame(self.janela)
        self.frame_botoesSessoes = tk.Frame(self.janela)
        self.frame_botoesLivros = tk.Frame(self.janela)

    def cadastrar_livro(self):
        self.lv1 = Livro()
        self.top_cadastro_livro = tk.Toplevel(self.janela)
        self.top_cadastro_livro.title('Cadastro de Livro')
        self.top_cadastro_livro.geometry("700x600")
        self.top_cadastro_livro.grab_set()

        caminho_logo2 = resource_path("logo_biblio2.png")
        self.icone2 = tk.PhotoImage(file=caminho_logo2)
        self.top_cadastro_livro.wm_iconphoto(False, self.icone2)

        self.str_nomeLivro = tk.StringVar()
        self.int_edicao = tk.IntVar()
        self.int_idEditora = tk.IntVar()
        self.int_idAutor = tk.IntVar()
        self.str_tipoLivro = tk.StringVar()
        self.int_sessao = tk.IntVar()

        self.frmCadLivro = Frame(self.top_cadastro_livro, padding=15)
        self.frmCadLivro.pack(anchor='center', expand=True, padx=20, pady=20)

        self.lbl_nomeLivro = ttk.Label(self.frmCadLivro, text='Nome:', font=self.fontelbl)
        self.lbl_nomeLivro.grid(row=0, column=0, sticky='w', pady=5, padx=5)
        self.cmp_nomeLivro = ttk.Entry(self.frmCadLivro, width=40, font=self.fonteent, textvariable=self.str_nomeLivro)
        self.cmp_nomeLivro.grid(row=0, column=1, pady=5, padx=5)

        self.lbl_nEdicao = ttk.Label(self.frmCadLivro, text='Número da Edição:', font=self.fontelbl)
        self.lbl_nEdicao.grid(row=1, column=0, sticky='w', pady=5, padx=5)
        self.cmp_nEdicao = ttk.Entry(self.frmCadLivro, width=40, font=self.fonteent, textvariable=self.int_edicao)
        self.cmp_nEdicao.grid(row=1, column=1, pady=5, padx=5)

        self.lbl_autorLivro = ttk.Label(self.frmCadLivro, text='Código do Autor:', font=self.fontelbl)
        self.lbl_autorLivro.grid(row=2, column=0, sticky='w', pady=5, padx=5)


        a1 = Autor()
        ids = a1.get_dado('id')
        self.opcoesAutor = [id for id in ids]
        self.combobox_autorLivro = ttk.Combobox(self.frmCadLivro, values=self.opcoesAutor, width=38, font=self.fonteent, textvariable=self.int_idAutor)
        self.combobox_autorLivro.grid(row=2, column=1, pady=5, padx=5)

        self.lbl_nmeEditora = ttk.Label(self.frmCadLivro, text='Código da Editora:', font=self.fontelbl)
        self.lbl_nmeEditora.grid(row=3, column=0, sticky='w', pady=5, padx=5)

        e1 = Editora()
        ids = e1.get_dado('id')
        self.opcoesEditora = [id for id in ids]
        self.cmp_nmeEditora = ttk.Combobox(self.frmCadLivro, values=self.opcoesEditora, width=38, font=self.fonteent, textvariable=self.int_idEditora)
        self.cmp_nmeEditora.grid(row=3, column=1, pady=5, padx=10)

        self.lbl_sessao = ttk.Label(self.frmCadLivro, text='Sessão:', font=self.fontelbl)
        self.lbl_sessao.grid(row=4, column=0, sticky='w', pady=5, padx=5)

        s1 = Sessao()
        ids = s1.get_dado('id')
        self.opcoesSessao = [id for id in ids]
        self.combobox_lblSessao = ttk.Combobox(self.frmCadLivro, values=self.opcoesSessao, width=38, font=self.fonteent, textvariable=self.int_sessao)
        self.combobox_lblSessao.grid(row=4, column=1, pady=5, padx=10)

        self.lbl_tipoLivro = ttk.Label(self.frmCadLivro, text='Tipo de Livro:', font=self.fontelbl)
        self.lbl_tipoLivro.grid(row=5, column=0, sticky='w', pady=5, padx=5)
        self.cmp_tipoLivro = ttk.Entry(self.frmCadLivro, width=40, font=self.fonteent, textvariable=self.str_tipoLivro)
        self.cmp_tipoLivro.grid(row=5, column=1, pady=5, padx=5)

        self.btnCadLivro = Button(self.frmCadLivro, text='CADASTRAR', command=self.concluir_cadastro_livro,width=25)
        self.btnCadLivro.grid(row=6, column=0, columnspan=2, pady=20, padx=5)


    def concluir_cadastro_livro(self):
        tlv1 = TipoLivro()
        tlv1.adicionar_TipoLivro(f'"{self.str_tipoLivro.get()}"')
        id_tvl1 = tlv1.get_dado('id')

        self.lv1.adicionar_livro(f'"{self.str_nomeLivro.get()}","{self.int_edicao.get()}","{self.int_idAutor.get()}","{id_tvl1[0]}","{self.int_idEditora.get()}","{self.int_sessao.get()}"')
        # atributos = f'"{self.nomeLivro}",{self.nEdicao},"{self.idAutor}","{self.idTipoLivro}","{self.idEditora},"{self.idSessao}"'
        self.top_cadastro_livro.destroy()
        Messagebox.show_info(f'Livro {self.str_nomeLivro.get()} cadastrado!', 'Sucesso')

    def exibir_livros(self):
        self.trevieewEditora.destroy()

        self.frame_botoesEditoras.destroy()
        self.frame_botoesAutores.destroy()
        self.frame_botoesSessoes.destroy()
        self.frame_botoesLivros.destroy()
        self.trevieewSessao.destroy()
        self.trevieewAutor.destroy()
        self.trevieewLivro.destroy()
        self.frame_botoesLivros.destroy()

        # rowdata = [
        #     ('A123', 'IzzyCo', 12),
        #     ('A136', 'Kimdee Inc.', 45),
        #     ('A158', 'Farmadding Co.', 36)
        # ]
        lv1 = Livro()
        self.livroGet = lv1.listar_livros()
        self.rowdataLivro = self.livroGet
        self.trevieewLivro = ttk.Treeview(self.janela, columns=['0','1','2','3','4'], show='headings', selectmode='browse', height=25)
        self.trevieewLivro.heading('0', text='ID')
        self.trevieewLivro.column('0',width=98,anchor='center')
        self.trevieewLivro.heading('1', text='Nome do Livro')
        self.trevieewLivro.column('1',anchor='center')
        self.trevieewLivro.heading('2',text='ID Autor')
        self.trevieewLivro.column('2',anchor='center')
        self.trevieewLivro.heading('3',text='ID Tipo do Livro')
        self.trevieewLivro.column('3',anchor='center')
        self.trevieewLivro.heading('4',text='ID Sessão')
        self.trevieewLivro.column('4',anchor='center')
        self.trevieewLivro.pack(fill=tk.Y, padx=25, pady=25)

        for row in self.livroGet:
            self.trevieewLivro.insert('','end',id=row[0],values=(row[0],row[1],row[4],row[3],row[6]))

        # # Frame para os botões
        self.frame_botoesLivros = tk.Frame(self.janela)
        self.frame_botoesLivros.pack(pady=10) 

        # Botão de excluir  
        self.btn_excluirLivro = ttk.Button(self.frame_botoesLivros, text="EXCLUIR", bootstyle="DANGER", command=lambda: self.excluir_livro(self.trevieewLivro.selection()) )
        self.btn_excluirLivro.pack(side=tk.LEFT, padx=5)

        # Botão de editar
        self.btn_editarLivro = ttk.Button(self.frame_botoesLivros, text="EDITAR", bootstyle="SUCCESS", command=lambda: self.editar_livro(self.trevieewLivro.selection()))
        self.btn_editarLivro.pack(side=tk.LEFT, padx=5)

        # Botão de atualizar
        self.btn_editarLivro = ttk.Button(self.frame_botoesLivros, text="ATUALIZAR TABELA", bootstyle="INFO", command=self.exibir_livros)
        self.btn_editarLivro.pack(side=tk.LEFT, padx=5)


    def excluir_livro(self, livro_selecionado):
        lv1 = Livro()
        id_livro = livro_selecionado[0]
        show_info = Messagebox.show_question(f"VOCÊ TEM CERTEZA QUE DESEJA DELETAR O LIVRO DE ID = {id_livro}",title='CONFIRMAÇÃO DE EXCLUSÃO')
        if show_info:
            lv1.excluir_livro(id_livro)

    def editar_livro(self, livro_selecionado):
        self.lv1 = Livro()
        self.id_livro = livro_selecionado[0]
        self.top_editarLivro = tk.Toplevel(self.janela)
        self.top_editarLivro.title('Editar Livro')
        self.top_editarLivro.geometry("600x600")  
        self.top_editarLivro.grab_set()

        self.icone2 = tk.PhotoImage(file=resource_path('logo_biblio3.png'))
        self.top_editarLivro.wm_iconphoto(False, self.icone2)

        self.str_nomeLivro = tk.StringVar()
        self.int_edicao = tk.IntVar()
        self.int_idEditora = tk.IntVar()
        self.int_idAutor = tk.IntVar()
        self.str_tipoLivro = tk.StringVar() 
        self.int_sessao = tk.IntVar()

        self.frmEdLivro = Frame(self.top_editarLivro, padding=15)
        self.frmEdLivro.pack(anchor='center', expand=True, padx=20, pady=20)

        self.lbl_nomeLivro = ttk.Label(self.frmEdLivro, text='Nome:', font=self.fontelbl)
        self.lbl_nomeLivro.grid(row=0, column=0, sticky='w', pady=5, padx=5)
        self.cmp_nomeLivro = ttk.Entry(self.frmEdLivro, width=40, font=self.fonteent, textvariable=self.str_nomeLivro)
        self.cmp_nomeLivro.insert(0, self.lv1.get_dado_livro('nomeLivro', self.id_livro))
        self.cmp_nomeLivro.grid(row=0, column=1, pady=5, padx=5)

    
        self.lbl_nEdicao = ttk.Label(self.frmEdLivro, text='N Edição:', font=self.fontelbl)
        self.lbl_nEdicao.grid(row=1, column=0, sticky='w', pady=5, padx=5)
        self.cmp_nEdicao = ttk.Entry(self.frmEdLivro, width=40, font=self.fonteent, textvariable=self.int_edicao)
        self.cmp_nEdicao.insert(0, self.lv1.get_dado_livro('edicao', self.id_livro))
        self.cmp_nEdicao.grid(row=1, column=1, pady=5, padx=5)

        self.lbl_autorLivro = ttk.Label(self.frmEdLivro, text='Autor:', font=self.fontelbl)
        self.lbl_autorLivro.grid(row=2, column=0, sticky='w', pady=5, padx=5)

        a1 = Autor()
        ids = a1.get_dado('id')
        self.opcoesAutor = [id for id in ids]
        self.combobox_autorLivro = ttk.Combobox(self.frmEdLivro, values=self.opcoesAutor, width=38, font=self.fonteent, textvariable=self.int_idAutor)
        self.combobox_autorLivro.grid(row=2, column=1, pady=5, padx=5)
        self.combobox_autorLivro.set(self.lv1.get_dado_livro('idAutor', self.id_livro))  # Usando set para selecionar

        self.lbl_nmeEditora = ttk.Label(self.frmEdLivro, text='Editora:', font=self.fontelbl)
        self.lbl_nmeEditora.grid(row=3, column=0, sticky='w', pady=5, padx=5)

        e1 = Editora()
        ids = e1.get_dado('id')
        self.opcoesEditora = [id for id in ids]
        self.cmp_nmeEditora = ttk.Combobox(self.frmEdLivro, values=self.opcoesEditora, width=38, font=self.fonteent, textvariable=self.int_idEditora)
        self.cmp_nmeEditora.grid(row=3, column=1, pady=5, padx=10)
        self.cmp_nmeEditora.set(self.lv1.get_dado_livro('idEditora', self.id_livro))

        self.lbl_sessao = ttk.Label(self.frmEdLivro, text='Sessão:', font=self.fontelbl)
        self.lbl_sessao.grid(row=4, column=0, sticky='w', pady=5, padx=5)

        s1 = Sessao()
        ids = s1.get_dado('id')
        self.opcoesSessao = [id for id in ids]
        self.combobox_lblSessao = ttk.Combobox(self.frmEdLivro, values=self.opcoesSessao, width=38, font=self.fonteent, textvariable=self.int_sessao)
        self.combobox_lblSessao.grid(row=4, column=1, pady=5, padx=10)
        self.combobox_lblSessao.set(self.lv1.get_dado_livro('idSessao', self.id_livro))

        self.lbl_tipoLivro = ttk.Label(self.frmEdLivro, text='Tipo de Livro:', font=self.fontelbl)
        self.lbl_tipoLivro.grid(row=5, column=0, sticky='w', pady=5, padx=5)
        self.cmp_tipoLivro = ttk.Entry(self.frmEdLivro, width=40, font=self.fonteent, textvariable=self.str_tipoLivro)
        self.cmp_tipoLivro.insert(0, self.lv1.get_dado_livro('idTipoLivro', self.id_livro))
        self.cmp_tipoLivro.grid(row=5, column=1, pady=5, padx=5)

        self.btnEditLivro = Button(self.frmEdLivro, text='EDITAR', command=self.concluir_editar_livro, width=25)
        self.btnEditLivro.grid(row=6, column=0, columnspan=2, pady=20, padx=5)



    def concluir_editar_livro(self):
        self.lv1.editar_livro(self.id_livro,self.str_nomeLivro.get(),self.int_edicao.get(),self.int_idAutor.get(),self.str_tipoLivro.get(),self.int_idEditora.get(),self.int_sessao.get())
        self.top_editarLivro.destroy()
        Messagebox.show_info('Edição feita.','Sucesso')
        
    def cadastrar_autor(self):
        self.at1 = Autor()
        self.top_cadastroAutor = tk.Toplevel(self.janela,width=100)
        self.top_cadastroAutor.title('Cadastro de Autor')
        self.top_cadastroAutor.grab_set()

        caminho_logo2 = resource_path("logo_biblio2.png")
        self.icone2 = tk.PhotoImage(file=caminho_logo2)
        self.top_cadastroAutor.wm_iconphoto(False, self.icone2)

        self.cadastroAutor = Frame(self.top_cadastroAutor, padding=10)
        self.cadastroAutor.pack(anchor='center', expand=True, side='left')


        self.str_nomeAutor = tk.StringVar()

        self.lbl_cadastroAutor = ttk.Label(self.cadastroAutor, text='Nome do Autor:', font=self.fontelbl)
        self.lbl_cadastroAutor.pack(anchor='center',padx=5,pady=5)
        self.cmpo_cadastroAutor = ttk.Entry(self.cadastroAutor, width=50, font=self.fonteent,textvariable=self.str_nomeAutor)
        self.cmpo_cadastroAutor.pack(anchor='center',padx=5,pady=5)
        self.btnCadAutor = Button(self.cadastroAutor, text='CADASTRAR', command=self.concluir_cadastro_autor)
        self.btnCadAutor.pack(anchor='center', expand=True, pady=10)

    def concluir_cadastro_autor(self):
        self.at1.adicionar_autor(f'"{self.str_nomeAutor.get()}"')
        self.top_cadastroAutor.destroy()
        Messagebox.show_info(f'Autor {self.str_nomeAutor.get()} cadastrado!', 'Sucesso')

    
    def exibir_autores(self):
        self.trevieewEditora.destroy()
        self.frame_botoesAutores.destroy()
        self.frame_botoesSessoes.destroy()
        self.frame_botoesEditoras.destroy()
        self.frame_botoesLivros.destroy()

        self.trevieewSessao.destroy()
        self.trevieewLivro.destroy()
        self.trevieewAutor.destroy()

        a1 = Autor()
        self.autorGet = a1.listar_autor()
        self.rowdataAutor = self.autorGet

        # rowdata = 
        self.trevieewAutor = ttk.Treeview(self.janela, columns=['0', '1'], show='headings', selectmode='browse', height=25)
        self.trevieewAutor.heading('0', text='ID')
        self.trevieewAutor.column('0',width=450,anchor='center')
        self.trevieewAutor.heading('1', text='Nome do Autor')
        self.trevieewAutor.column('1',width=450,anchor='center')
        self.trevieewAutor.pack(fill=tk.Y, padx=25, pady=25)

        for row in self.autorGet:
            self.trevieewAutor.insert('','end',id=row[0],values=(row[0],row[1]))

        # # Frame para os botões
        self.frame_botoesAutores = tk.Frame(self.janela)
        self.frame_botoesAutores.pack(pady=10) 

        # Botão de excluir  
        self.btn_excluirAutor = ttk.Button(self.frame_botoesAutores, text="EXCLUIR", bootstyle="DANGER", command=lambda: self.excluir_autor(self.trevieewAutor.selection()) )
        self.btn_excluirAutor.pack(side=tk.LEFT, padx=5)

        # Botão de editar
        self.btn_editarAutor = ttk.Button(self.frame_botoesAutores, text="EDITAR", bootstyle="SUCCESS", command=lambda: self.editar_autor(self.trevieewAutor.selection()))
        self.btn_editarAutor.pack(side=tk.LEFT, padx=5)

        # Botão de atualizar
        self.btn_editarAutor = ttk.Button(self.frame_botoesAutores, text="ATUALIZAR TABELA", bootstyle="INFO", command=self.exibir_autores)
        self.btn_editarAutor.pack(side=tk.LEFT, padx=5)

    def excluir_autor(self,autor_selecionada):
        a1 = Autor()
        id_autor = autor_selecionada[0]
        show_info = Messagebox.show_question(f"VOCÊ TEM CERTEZA QUE DESEJA DELETAR O AUTOR DE ID = {id_autor}",title='CONFIRMAÇÃO DE EXCLUSÃO')
        if show_info:
            a1.excluir_autor(id_autor)

    def editar_autor(self,autor_selecionada):
        self.a1 = Autor()
        self.id_autor = autor_selecionada[0]

        self.top_edicaoAutor = tk.Toplevel(self.janela,width=100)
        self.top_edicaoAutor.title('Edição de Autor')
        self.top_edicaoAutor.grab_set()

        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file=resource_path('logo_biblio3.png'))
        self.top_edicaoAutor.wm_iconphoto(False, self.icone2)

        self.edicaoAutor = Frame(self.top_edicaoAutor, padding=10)
        self.edicaoAutor.pack(anchor='center', expand=True, side='left')

        self.str_nomeAutor = tk.StringVar()

        self.lbl_edicaoAutor = ttk.Label(self.edicaoAutor, text='Nome do Autor:', font=self.fontelbl)
        self.lbl_edicaoAutor.pack(anchor='center',padx=5,pady=5)
        self.cmpo_edicaoAutor = ttk.Entry(self.edicaoAutor, width=50, font=self.fonteent,textvariable=self.str_nomeAutor)
        self.cmpo_edicaoAutor.insert(0,self.a1.get_dado_autor('nomeAutor',self.id_autor))
        self.cmpo_edicaoAutor.pack(anchor='center',padx=5,pady=5)
        self.btnEdiAutor = Button(self.edicaoAutor, text='EDITAR',command=self.concluir_editar_autor)
        self.btnEdiAutor.pack(anchor='center', expand=True, pady=10)

    def concluir_editar_autor(self):
        self.a1.editar_autor(self.id_autor,self.str_nomeAutor.get())
        self.top_edicaoAutor.destroy()
        Messagebox.show_info('Edição feita.','Sucesso')

    def cadastrar_sessao(self):
        self.s1 = Sessao()
        self.top_cadastroSessao = tk.Toplevel(self.janela,width=100)
        self.top_cadastroSessao.title('Cadastro de Sessão')
        self.top_cadastroSessao.grab_set()
        caminho_logo2 = resource_path("logo_biblio2.png")
        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file=caminho_logo2)
        self.top_cadastroSessao.wm_iconphoto(False, self.icone2)

        self.str_nomeSessao = tk.StringVar()
        self.str_descrSessao = tk.StringVar()
        self.str_statusSessao = tk.StringVar()
        self.frmCadSessao = Frame(self.top_cadastroSessao, padding=15)
        self.frmCadSessao.pack(anchor='center', expand=True, padx=20,pady=20)
        
        self.lbl_nomeSessao = ttk.Label(self.frmCadSessao, text='Nome:', font=self.fontelbl)
        self.lbl_nomeSessao.grid(row=0,column=0,sticky='w',padx=5,pady=5)
        self.cmp_nomeSessao = ttk.Entry(self.frmCadSessao, width=50, font=self.fonteent,textvariable=self.str_nomeSessao)
        self.cmp_nomeSessao.grid(row=0,column=1,pady=5,padx=5)

        self.lbl_descrSessao = ttk.Label(self.frmCadSessao,text='Descrição: ',font=self.fontelbl)
        self.lbl_descrSessao.grid(row=1,column=0,sticky='w',padx=5,pady=5)
        self.cmp_descrSessao = ttk.Entry(self.frmCadSessao,width=50,font=self.fonteent,textvariable=self.str_descrSessao)
        self.cmp_descrSessao.grid(row=1,column=1,padx=5,pady=10)

        self.opcoes = ["A","I"]
        self.lbl_statusSessao = ttk.Label(self.frmCadSessao,text="Status:",font=self.fontelbl)
        self.lbl_statusSessao.grid(row=2,column=0,sticky='w',padx=5,pady=5)
        self.combobox_statusSessao = ttk.Combobox(self.frmCadSessao, values=self.opcoes,width=48, font=self.fonteent,textvariable=self.str_statusSessao)
        self.combobox_statusSessao.grid(row=2,column=1,padx = 10,pady=5)
        dados = f'"{self.cmp_nomeSessao.get()}","{self.str_descrSessao.get()}","{self.str_statusSessao.get()}"'
        self.btnCadSessao = Button(self.frmCadSessao, text='CADASTRAR',command=self.concluir_cadastro_sessao)
        self.btnCadSessao.grid(row=3,column=0,columnspan=2,pady=20,padx=5)

    def concluir_cadastro_sessao(self):
        self.s1.adicionar_Sessao(f'"{self.cmp_nomeSessao.get()}","{self.str_descrSessao.get()}","{self.str_statusSessao.get()}"')
        self.top_cadastroSessao.destroy()
        Messagebox.show_info(f'Sessão {self.str_nomeSessao.get()} cadastrada!', 'Sucesso')
    def exibir_sessoes(self):
        s1 = Sessao()
        self.sessao_get = s1.listar_Sessao()
        self.row_dataSessao = self.sessao_get
        self.frame_botoesAutores.destroy()
        self.frame_botoesSessoes.destroy()
        self.frame_botoesEditoras.destroy()
        self.frame_botoesLivros.destroy()

        self.trevieewAutor.destroy()
        self.trevieewLivro.destroy()
        self.trevieewSessao.destroy()
        self.trevieewEditora.destroy()
        
        self.trevieewSessao = ttk.Treeview(self.janela, columns=['0', '1','2'], show='headings', selectmode='browse', height=25)
        self.trevieewSessao.heading('0', text='ID')
        self.trevieewSessao.column('0',width=300,anchor='center')
        self.trevieewSessao.heading('1', text='Nome da Sessao')
        self.trevieewSessao.column('1',width=300,anchor='center')
        self.trevieewSessao.heading('2',text='Status')
        self.trevieewSessao.column('2',width=300,anchor='center')
        self.trevieewSessao.pack(fill=tk.Y, padx=25, pady=25)

        for row in self.row_dataSessao:
            self.trevieewSessao.insert('','end',id=row[0],values=(row[0],row[1],row[3]))

           # # Frame para os botões
        self.frame_botoesSessoes = tk.Frame(self.janela)
        self.frame_botoesSessoes.pack(pady=10) 

        # Botão de excluir  
        self.btn_excluirSessao = ttk.Button(self.frame_botoesSessoes, text="EXCLUIR", bootstyle="DANGER", command=lambda: self.excluir_Sessao(self.trevieewSessao.selection()) )
        self.btn_excluirSessao.pack(side=tk.LEFT, padx=5)

        # Botão de editar
        self.btn_editarSessao = ttk.Button(self.frame_botoesSessoes, text="EDITAR", bootstyle="SUCCESS",command=lambda: self.editar_Sessao(self.trevieewSessao.selection()))
        self.btn_editarSessao.pack(side=tk.LEFT, padx=5)

        # Botão de atualizar
        self.btn_atualizarSessao = ttk.Button(self.frame_botoesSessoes, text="ATUALIZAR TABELA", bootstyle="INFO", command=self.exibir_sessoes)
        self.btn_atualizarSessao.pack(side=tk.LEFT, padx=5)

        
    def excluir_Sessao(self,sessao_selecionada):
        s1 = Sessao()
        id_sessao = sessao_selecionada[0]
        show_info = Messagebox.show_question(f"VOCÊ TEM CERTEZA QUE DESEJA DELETAR A SESSÃO DE ID = {id_sessao}",title='CONFIRMAÇÃO DE EXCLUSÃO')
        if show_info:
            s1.excluir_Sessao(id_sessao)
    
    def editar_Sessao(self,sessao_selecionada):
        self.s1 = Sessao()
        self.id_sessao = sessao_selecionada[0]
        self.top_editarSessao = tk.Toplevel(self.janela,width=100)
        self.top_editarSessao.title('Editar de Sessão')
        self.top_editarSessao.grab_set()

        self.icone2 = tk.PhotoImage(file=resource_path('logo_biblio3.png'))
        self.top_editarSessao.wm_iconphoto(False, self.icone2)

        self.str_nomeSessao = tk.StringVar()
        self.str_descrSessao = tk.StringVar()
        self.str_statusSessao = tk.StringVar()
        self.frmeditSessao = Frame(self.top_editarSessao, padding=10)
        self.frmeditSessao.pack(anchor='center', expand=True, side='left')
        
        self.lbl_nomeSessao = ttk.Label(self.frmeditSessao, text='Nome:', font=self.fontelbl)
        self.lbl_nomeSessao.pack(anchor='center')
        self.cmp_nomeSessao = ttk.Entry(self.frmeditSessao, width=50, font=self.fonteent,textvariable=self.str_nomeSessao)
        self.cmp_nomeSessao.insert(0,self.s1.get_dado_Sessao('nomeSessao',self.id_sessao))
        self.cmp_nomeSessao.pack(anchor='center')

        self.lbl_descrSessao = ttk.Label(self.frmeditSessao,text='Descrição',font=self.fontelbl)
        self.lbl_descrSessao.pack(anchor='center')
        self.cmp_descrSessao = ttk.Entry(self.frmeditSessao,width=50,font=self.fonteent,textvariable=self.str_descrSessao)
        self.cmp_descrSessao.insert(1,self.s1.get_dado_Sessao('descr',self.id_sessao))
        self.cmp_descrSessao.pack(anchor='center')

        self.opcoes = ["A","I"]
        self.lbl_statusSessao = ttk.Label(self.frmeditSessao,text="Status",font=self.fontelbl)
        self.lbl_statusSessao.pack(anchor='center')
        self.combobox_statusSessao = ttk.Combobox(self.frmeditSessao, values=self.opcoes,width=50, font=self.fonteent,textvariable=self.str_statusSessao)
        self.combobox_statusSessao.set(self.s1.get_dado_Sessao('status',self.id_sessao))
        self.combobox_statusSessao.pack()
    
        self.btnEditSessao = Button(self.frmeditSessao, text='EDITAR',command=self.concluir_editar_sessao)
        self.btnEditSessao.pack(anchor='center', expand=True, pady=10)

    def concluir_editar_sessao(self):
        self.s1.editar_Sessao(self.id_sessao,self.str_nomeSessao.get(),self.str_descrSessao.get(),self.str_statusSessao.get())
        self.top_editarSessao.destroy()
        Messagebox.show_info('Edição feita.','Sucesso')    

    def cadastrar_editora(self):
        self.ed1 = Editora()
        self.top_cadastroEditora = tk.Toplevel(self.janela,width=100)
        self.top_cadastroEditora.title('Cadastro de Editora')
        self.top_cadastroEditora.grab_set()
        caminho_logo2 = resource_path("logo_biblio2.png")
        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file=caminho_logo2)
        self.top_cadastroEditora.wm_iconphoto(False, self.icone2)

        self.cadastroEditora = Frame(self.top_cadastroEditora, padding=10)
        self.cadastroEditora.pack(anchor='center', expand=True, side='left')


        self.str_nomeEditora = tk.StringVar()

        self.lbl_cadastroEditora = ttk.Label(self.cadastroEditora, text='Nome da Editora:', font=self.fontelbl)
        self.lbl_cadastroEditora.pack(anchor='center',padx=5,pady=5)
        self.cmpo_cadastroEditora = ttk.Entry(self.cadastroEditora, width=50, font=self.fonteent,textvariable=self.str_nomeEditora)
        self.cmpo_cadastroEditora.pack(anchor='center',padx=5,pady=5)
        self.btnCadEditora = Button(self.cadastroEditora, text='CADASTRAR', command=self.concluir_cadastro_editora)
        self.btnCadEditora.pack(anchor='center', expand=True, pady=10)

    def concluir_cadastro_editora(self):
        self.ed1.adicionar_editora(f'"{self.str_nomeEditora.get()}"')
        self.top_cadastroEditora.destroy()
        Messagebox.show_info(f'Editora {self.str_nomeEditora.get()} cadastrada!', 'Sucesso')

    def exibir_editoras(self):
        # Limpa os widgets anteriores
        self.trevieewEditora.destroy()
        self.frame_botoesEditoras.destroy()
        self.frame_botoesSessoes.destroy()
        self.frame_botoesAutores.destroy()
        self.frame_botoesLivros.destroy()

        self.trevieewAutor.destroy()
        self.trevieewLivro.destroy()
        self.trevieewSessao.destroy()
        
        e1 = Editora()
        self.editora_get = e1.listar_editora()
        self.rowdataEditora = self.editora_get

        self.trevieewEditora = ttk.Treeview(self.janela, columns=['0', '1'], show='headings', selectmode='browse', height=25)
        self.trevieewEditora.heading('0', text='ID')
        self.trevieewEditora.column('0',width=450,anchor='center')
        self.trevieewEditora.heading('1', text='Nome da Editora')
        self.trevieewEditora.column('1',width=450,anchor='center')
        self.trevieewEditora.pack(fill=tk.Y, padx=25, pady=25)

        for row in self.editora_get:
            self.trevieewEditora.insert('', 'end', id=row[0], values=(row[0], row[1]))

    
        # # Frame para os botões
        self.frame_botoesEditoras = tk.Frame(self.janela)
        self.frame_botoesEditoras.pack(pady=10) 

        # Botão de excluir  
        self.btn_excluirEditora = ttk.Button(self.frame_botoesEditoras, text="EXCLUIR", bootstyle="DANGER", command=lambda: self.excluir_editora(self.trevieewEditora.selection()) )
        self.btn_excluirEditora.pack(side=tk.LEFT, padx=5)

        # Botão de editar
        self.btn_editarEditora = ttk.Button(self.frame_botoesEditoras, text="EDITAR", bootstyle="SUCCESS", command=lambda: self.editar_editora(self.trevieewEditora.selection()))
        self.btn_editarEditora.pack(side=tk.LEFT, padx=5)

        # Botão de atualizar
        self.btn_editarEditora = ttk.Button(self.frame_botoesEditoras, text="ATUALIZAR TABELA", bootstyle="INFO", command=self.exibir_editoras)
        self.btn_editarEditora.pack(side=tk.LEFT, padx=5)

        

    def excluir_editora(self,editora_selecionada):
        e1 = Editora()
        id_editora = editora_selecionada[0]
        show_info = Messagebox.show_question(f"VOCÊ TEM CERTEZA QUE DESEJA DELETAR A EDITORA DE ID = {id_editora}",title='CONFIRMAÇÃO DE EXCLUSÃO')
        if show_info:
            e1.excluir_editora(id_editora)

    def editar_editora(self,editora_selecionada):
        self.e1 = Editora()
        self.id_editora = editora_selecionada[0]

        self.top_edicaoEditora = tk.Toplevel(self.janela,width=100)
        self.top_edicaoEditora.title('Edição de Livro')
        self.top_edicaoEditora.grab_set()
        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file=resource_path('logo_biblio3.png'))
        self.top_edicaoEditora.wm_iconphoto(False, self.icone2)

        self.edicaoEditora = Frame(self.top_edicaoEditora, padding=10)
        self.edicaoEditora.pack(anchor='center', expand=True, side='left')

        

        self.str_nomeEditora = tk.StringVar()

        self.lbl_edicaoEditora = ttk.Label(self.edicaoEditora, text='Nome da Editora:', font=self.fontelbl)
        self.lbl_edicaoEditora.pack(anchor='center',padx=5,pady=5)
        self.cmpo_edicaoEditora = ttk.Entry(self.edicaoEditora, width=50, font=self.fonteent,textvariable=self.str_nomeEditora)
        self.cmpo_edicaoEditora.insert(0,self.e1.get_dado_editora('nomeEditora',self.id_editora))
        self.cmpo_edicaoEditora.pack(anchor='center',padx=5,pady=5)
        self.btnEdiEditora = Button(self.edicaoEditora, text='EDITAR',command=self.concluir_editar_editora)
        self.btnEdiEditora.pack(anchor='center', expand=True, pady=10)

    def concluir_editar_editora(self):
        self.e1.editar_editora(self.id_editora,self.str_nomeEditora.get())
        self.top_edicaoEditora.destroy()
        Messagebox.show_info('Edição feita.','Sucesso')

    def alterar_tema(self):
        self.top_mudarTema = tk.Toplevel(self.janela,width=100)
        self.top_mudarTema.title('Mudança de Tema')
        self.top_mudarTema.grab_set()

        frmTema = Frame(self.top_mudarTema, padding=10)
        frmTema.pack()

        self.temas = ('Morph', 'Journal', 'Darkly', 'Superhero', 'Solar', 'Cyborg', 'Vapor', 'Simplex', 'Cerculean',
                'Cosmo', 'Flatly', 'Litera', 'Minty', 'Lumen', 'Sandstone', 'Yeti', 'Pulse', 'United')
        self.cbx_temas = Combobox(frmTema, values=self.temas, font=self.fonteent)
        self.cbx_temas.pack()

        self.btnConfirmarTema = Button(frmTema, text='CONFIRMAR', command=self.concluir_mudanca_tema)
        self.btnConfirmarTema.pack(pady=10)
        
    def concluir_mudanca_tema(self):
        temaSelecionado = self.cbx_temas.get()
        self.janela.style.theme_use(temaSelecionado.lower())


janela = ttk.Window(themename='cyborg')
janela.resizable(False, False)
janela.wm_iconposition(10, 10)
janela.geometry("1080x720")
app = TelaLogin(janela)
janela.mainloop()
