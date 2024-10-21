import ttkbootstrap as ttk


class TelaLogin:
    def __init__(self, master):
        self.janela = master

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


janela = ttk.Window()
janela.resizable(False, False)
janela.wm_iconposition(10, 10)
janela.geometry("1080x720")
app = TelaLogin(janela)
janela.mainloop()
