import ttkbootstrap as ttk
from ttkbootstrap import Frame, Label, Entry, Button, Combobox
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import tkinter as tk
from autor import Autor
from editora import Editora
from ttkbootstrap.dialogs import Messagebox

from sessao import Sessao

class TelaLogin:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Biblioteca Pessoal')

        # alteração do ícone da janela
        self.icone = tk.PhotoImage(file='logo_biblio.png')
        self.janela.wm_iconphoto(False, self.icone)

        # fontes padrão
        self.fontelbl = ttk.font.Font(size=16, weight='bold')
        self.fonteent = ttk.font.Font(size=16, weight='normal')

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
        self.entUser.pack()

        self.lblSenha = Label(self.frmLoginR, text='Senha:', font=self.fontelbl)
        self.lblSenha.pack(anchor='w')
        self.entSenha = Entry(self.frmLoginR, font=self.fonteent)
        self.entSenha.pack()

        self.btnEntrar = Button(self.frmLoginR, text='ENTRAR',command=self.entrar_sistema)
        self.btnEntrar.pack(pady=10)
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

        self.menu.add_cascade(label='LIVROS', menu=self.mnu_livros, font=self.fontelbl)
        self.menu.add_cascade(label='AUTORES', menu=self.mnu_autores)
        self.menu.add_cascade(label='SESSÕES', menu=self.mnu_sessoes)
        self.menu.add_cascade(label="EDITORAS",menu=self.mnu_editoras)

        self.mnu_livros.add_command(label='Cadastrar Livro', command=self.cadastrar_livro)
        self.mnu_livros.add_command(label='Visualizar Livro',command=self.exibir_livros)

        self.mnu_autores.add_command(label='Cadastrar Autor',command=None)
        self.mnu_autores.add_command(label='Visualizar Autores',command=self.exibir_autores)

        self.mnu_sessoes.add_command(label='Cadastrar Sessão',command=self.cadastrar_sessao)
        self.mnu_sessoes.add_command(label='Visualizar Sessão',command=self.exibir_sessoes)

        self.mnu_editoras.add_command(label="Cadastrar Editora",command=self.cadastrar_editora)
        self.mnu_editoras.add_command(label="Visualizar Editora",command=self.exibir_editoras)

        self.janela.config(menu=self.menu)
        
    def cadastrar_livro(self):
        self.top_cadastro_livro = tk.Toplevel(self.janela,width=100)
        self.top_cadastro_livro.title('Cadastro de Livro')
        self.top_cadastro_livro.grab_set()

        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file='logo_biblio2.png')
        self.top_cadastro_livro.wm_iconphoto(False, self.icone2)

        # def atualizar_label(janela):
            # if combobox.get()=="Novo Autor":
            #     nvoLivro = ttk.Label(janela,text='Digite o novo autor')
            #     nvoLivro.pack()
            #     cmpNvoLivro = ttk.Entry(janela)
            #     cmpNvoLivro.pack()

        self.frmCadLivro = Frame(self.top_cadastro_livro, padding=10)
        self.frmCadLivro.pack(anchor='center', expand=True, side='left')
        
        self.lbl_nomeLivro = ttk.Label(self.frmCadLivro, text='Nome:', font=self.fontelbl)
        self.lbl_nomeLivro.pack(anchor='center')
        self.cmp_nomeLivro = ttk.Entry(self.frmCadLivro, width=50, font=self.fonteent)
        self.cmp_nomeLivro.pack(anchor='center')

        self.lbl_autorLivro = ttk.Label(self.frmCadLivro, text='Autor:', font=self.fontelbl)
        self.lbl_autorLivro.pack(anchor='center')
        self.opcoes = ["Novo Autor", "Opção 2", "Opção 3", "Opção 4"]
        self.combobox_autorLivro = ttk.Combobox(self.frmCadLivro, values=self.opcoes,width=50, font=self.fonteent)
        self.combobox_autorLivro.pack(padx=40)

        self.frmEdSes = Frame(self.frmCadLivro)
        self.frmEdSes.pack(anchor='center', expand=True)
        
        self.lbl_nmeEditora = ttk.Label(self.frmEdSes,text='Editora', font=self.fontelbl)
        self.lbl_nmeEditora.grid(row=0, column=0, sticky='w')
        #self.lbl_nmeEditora.pack(anchor='w',padx=40)

        self.lbl_sessao = ttk.Label(self.frmEdSes,text='Número da Sessão', font=self.fontelbl)
        self.lbl_sessao.grid(row=0, column=1, sticky='e')
        #self.lbl_sessao.pack(anchor='e',padx=40)

        self.opcoesSessao = [1,2,3,4,5,6,7]

        self.cmp_nmeEditora = Combobox(self.frmEdSes,values=self.opcoesSessao,width=25, font=self.fonteent)
        self.cmp_nmeEditora.grid(row=1, column=0)
        #self.cmp_nmeEditora.pack(side='left',anchor='w',pady=30,padx=20)

        self.combobox_lblSessao = Combobox(self.frmEdSes,values=self.opcoesSessao,width=25, font=self.fonteent)
        self.combobox_lblSessao.grid(row=1, column=1)
        #self.combobox_lblSessao.pack(side='right',anchor='e',pady=30,padx=20)

        self.btnCadLivro = Button(self.frmCadLivro, text='CADASTRAR')
        self.btnCadLivro.pack(anchor='center', expand=True, pady=10)

        #nome, edição, tipo, sessão, autor, editora

    def exibir_livros(self):
        self.trevieewEditora.destroy()
        self.frame_botoesEditoras.destroy()
        self.trevieewSessao.destroy()
        self.trevieewAutor.destroy()
        self.trevieewLivro.destroy()

        # rowdata = [
        #     ('A123', 'IzzyCo', 12),
        #     ('A136', 'Kimdee Inc.', 45),
        #     ('A158', 'Farmadding Co.', 36)
        # ]

        self.trevieewLivro = ttk.Treeview(self.janela, columns=['0','1','2','3','4'], show='headings', selectmode='browse', height=25)
        self.trevieewLivro.heading('0', text='ID')
        self.trevieewLivro.column('0',width=98,anchor='center')
        self.trevieewLivro.heading('1', text='Nome do Livro')
        self.trevieewLivro.heading('2',text='ID Autor')
        self.trevieewLivro.heading('3',text='ID Tipo do Livro')
        self.trevieewLivro.heading('4',text='ID Sessão')
        self.trevieewLivro.pack(fill=tk.Y, padx=25, pady=25)

    
    def exibir_autores(self):
        self.trevieewEditora.destroy()
        self.frame_botoesEditoras.destroy()

        self.trevieewSessao.destroy()
        self.trevieewLivro.destroy()
        self.trevieewAutor.destroy()

        autorGet = self.autor.listar_autor()
        self.rowdataAutor = autorGet

        # rowdata = 
        self.trevieewAutor = ttk.Treeview(self.janela, columns=['0', '1'], show='headings', selectmode='browse', height=25)
        self.trevieewAutor.heading('0', text='ID')
        self.trevieewAutor.column('0',width=450,anchor='center')
        self.trevieewAutor.heading('1', text='Nome do Autor')
        self.trevieewAutor.column('1',width=450,anchor='center')
        self.trevieewAutor.pack(fill=tk.Y, padx=25, pady=25)


    def cadastrar_sessao(self):
        s1 = Sessao()
        self.top_cadastroSessao = tk.Toplevel(self.janela,width=100)
        self.top_cadastroSessao.title('Cadastro de Livro')
        self.top_cadastroSessao.grab_set()

        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file='logo_biblio2.png')
        self.top_cadastroSessao.wm_iconphoto(False, self.icone2)

        # def atualizar_label(janela):
            # if combobox.get()=="Novo Autor":
            #     nvoLivro = ttk.Label(janela,text='Digite o novo autor')
            #     nvoLivro.pack()
            #     cmpNvoLivro = ttk.Entry(janela)
            #     cmpNvoLivro.pack()


        self.str_nomeSessao = tk.StringVar()
        self.str_descrSessao = tk.StringVar()
        self.str_statusSessao = tk.StringVar()
        self.frmCadSessao = Frame(self.top_cadastroSessao, padding=10)
        self.frmCadSessao.pack(anchor='center', expand=True, side='left')
        
        self.lbl_nomeSessao = ttk.Label(self.frmCadSessao, text='Nome:', font=self.fontelbl)
        self.lbl_nomeSessao.pack(anchor='center')
        self.cmp_nomeSessao = ttk.Entry(self.frmCadSessao, width=50, font=self.fonteent,textvariable=self.str_nomeSessao)
        self.cmp_nomeSessao.pack(anchor='center')

        self.lbl_descrSessao = ttk.Label(self.frmCadSessao,text='Descrição',font=self.fontelbl)
        self.lbl_descrSessao.pack(anchor='center')
        self.cmp_descrSessao = ttk.Entry(self.frmCadSessao,width=50,font=self.fonteent,textvariable=self.str_descrSessao)
        self.cmp_descrSessao.pack(anchor='center')

        self.opcoes = ["A","I"]
        self.lbl_statusSessao = ttk.Label(self.frmCadSessao,text="Status",font=self.fontelbl)
        self.lbl_statusSessao.pack(anchor='center')
        self.combobox_statusSessao = ttk.Combobox(self.frmCadSessao, values=self.opcoes,width=50, font=self.fonteent,textvariable=self.str_statusSessao)
        self.combobox_statusSessao.pack()
        dados = f'"{self.cmp_nomeSessao.get()}","{self.str_descrSessao.get()}","{self.str_statusSessao.get()}"'
        self.btnCadSessao = Button(self.frmCadSessao, text='CADASTRAR',command=lambda: s1.adicionar_Sessao(f'"{self.cmp_nomeSessao.get()}","{self.str_descrSessao.get()}","{self.str_statusSessao.get()}"'))
        self.btnCadSessao.pack(anchor='center', expand=True, pady=10)
    def exibir_sessoes(self):
        s1 = Sessao()
        self.sessao_get = s1.listar_Sessao()
        self.row_dataSessao = self.sessao_get
        self.trevieewEditora.destroy()
        self.frame_botoesEditoras.destroy()

        self.trevieewAutor.destroy()
        self.trevieewLivro.destroy()
        self.trevieewSessao.destroy()
        
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

        
    def excluir_Sessao(self,sessao_selecionada):
        s1 = Sessao()
        id_sessao = sessao_selecionada[0]
        show_info = Messagebox.show_question(f"VOCÊ TEM CERTEZA QUE DESEJA DELETAR A SESSÕA DE ID = {id_sessao}",title='CONFIRMAÇÃO DE EXCLUSÃO')
        if show_info:
            s1.excluir_Sessao(id_sessao)
    
    def editar_Sessao(self,sessao_selecionada):
        s1 = Sessao()
        id_sessao = sessao_selecionada[0]
        self.top_editarSessao = tk.Toplevel(self.janela,width=100)
        self.top_editarSessao.title('Editar de Livro')
        self.top_editarSessao.grab_set()

        self.icone2 = tk.PhotoImage(file='logo_biblio2.png')
        self.top_editarSessao.wm_iconphoto(False, self.icone2)

        

        self.str_nomeSessao = tk.StringVar()
        self.str_descrSessao = tk.StringVar()
        self.str_statusSessao = tk.StringVar()
        self.frmeditSessao = Frame(self.top_editarSessao, padding=10)
        self.frmeditSessao.pack(anchor='center', expand=True, side='left')
        
        self.lbl_nomeSessao = ttk.Label(self.frmeditSessao, text='Nome:', font=self.fontelbl)
        self.lbl_nomeSessao.pack(anchor='center')
        self.cmp_nomeSessao = ttk.Entry(self.frmeditSessao, width=50, font=self.fonteent,textvariable=self.str_nomeSessao)
        self.cmp_nomeSessao.insert(0,s1.get_dado_Sessao('nomeSessao',id_sessao))
        self.cmp_nomeSessao.pack(anchor='center')

        self.lbl_descrSessao = ttk.Label(self.frmeditSessao,text='Descrição',font=self.fontelbl)
        self.lbl_descrSessao.pack(anchor='center')
        self.cmp_descrSessao = ttk.Entry(self.frmeditSessao,width=50,font=self.fonteent,textvariable=self.str_descrSessao)
        self.cmp_descrSessao.insert(1,s1.get_dado_Sessao('descr',id_sessao))
        self.cmp_descrSessao.pack(anchor='center')

        self.opcoes = ["A","I"]
        self.lbl_statusSessao = ttk.Label(self.frmeditSessao,text="Status",font=self.fontelbl)
        self.lbl_statusSessao.pack(anchor='center')
        self.combobox_statusSessao = ttk.Combobox(self.frmeditSessao, values=self.opcoes,width=50, font=self.fonteent,textvariable=self.str_statusSessao)
        self.combobox_statusSessao.set(s1.get_dado_Sessao('status',id_sessao))
        self.combobox_statusSessao.pack()
    
        self.btnEditSessao = Button(self.frmeditSessao, text='EDITAR',command=lambda: s1.editar_Sessao(id_sessao))
        self.btnEditSessao.pack(anchor='center', expand=True, pady=10)

    def cadastrar_editora(self):
        ed1 = Editora()
        self.top_cadastroEditora = tk.Toplevel(self.janela,width=100)
        self.top_cadastroEditora.title('Cadastro de Livro')
        self.top_cadastroEditora.grab_set()

        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file='logo_biblio2.png')
        self.top_cadastroEditora.wm_iconphoto(False, self.icone2)

        self.cadastroEditora = Frame(self.top_cadastroEditora, padding=10)
        self.cadastroEditora.pack(anchor='center', expand=True, side='left')


        self.str_nomeEditora = tk.StringVar()

        self.lbl_cadastroEditora = ttk.Label(self.cadastroEditora, text='Nome da Editora:', font=self.fontelbl)
        self.lbl_cadastroEditora.pack(anchor='center')
        self.cmpo_cadastroEditora = ttk.Entry(self.cadastroEditora, width=50, font=self.fonteent,textvariable=self.str_nomeEditora)
        self.cmpo_cadastroEditora.pack(anchor='center')
        self.btnCadEditora = Button(self.cadastroEditora, text='CADASTRAR', command=lambda: ed1.adicionar_editora(f'"{self.str_nomeEditora.get()}"'))
        self.btnCadEditora.pack(anchor='center', expand=True, pady=10)



    def exibir_editoras(self):
        # Limpa os widgets anteriores
        self.trevieewEditora.destroy()
        self.frame_botoesEditoras.destroy()
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
        self.btn_editarEditora = ttk.Button(self.frame_botoesEditoras, text="EDITAR", bootstyle="SUCCESS",command=lambda: self.editar_editora(self.trevieewEditora.selection()))
        self.btn_editarEditora.pack(side=tk.LEFT, padx=5)

        

    def excluir_editora(self,editora_selecionada):
        e1 = Editora()
        id_editora = editora_selecionada[0]
        show_info = Messagebox.show_question(f"VOCÊ TEM CERTEZA QUE DESEJA DELETAR A EDITORA DE ID = {id_editora}",title='CONFIRMAÇÃO DE EXCLUSÃO')
        if show_info:
            e1.excluir_editora(id_editora)

    def editar_editora(self,editora_selecionada):
        e1 = Editora()
        id_editora = editora_selecionada[0]

        self.top_edicaoEditora = tk.Toplevel(self.janela,width=100)
        self.top_edicaoEditora.title('edicao de Livro')
        self.top_edicaoEditora.grab_set()

        # alteração do ícone da janela
        self.icone2 = tk.PhotoImage(file='logo_biblio2.png')
        self.top_edicaoEditora.wm_iconphoto(False, self.icone2)

        self.edicaoEditora = Frame(self.top_edicaoEditora, padding=10)
        self.edicaoEditora.pack(anchor='center', expand=True, side='left')

        

        self.str_nomeEditora = tk.StringVar()

        self.lbl_edicaoEditora = ttk.Label(self.edicaoEditora, text='Nome da Editora:', font=self.fontelbl)
        self.lbl_edicaoEditora.pack(anchor='center')
        self.cmpo_edicaoEditora = ttk.Entry(self.edicaoEditora, width=50, font=self.fonteent,textvariable=self.str_nomeEditora)
        self.cmpo_edicaoEditora.insert(0,e1.get_dado_editora('nomeEditora',id_editora))
        self.cmpo_edicaoEditora.pack(anchor='center')
        self.btnEdiEditora = Button(self.edicaoEditora, text='EDITAR',command=lambda:e1.editar_editora(id_editora,self.str_nomeEditora.get()))
        self.btnEdiEditora.pack(anchor='center', expand=True, pady=10)



janela = ttk.Window(themename='vapor')
janela.resizable(False, False)
janela.wm_iconposition(10, 10)
janela.geometry("1080x720")
app = TelaLogin(janela)
janela.mainloop()
