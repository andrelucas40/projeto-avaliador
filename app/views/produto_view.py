import tkinter as tk

class ProdutoView:
    def __init__(self, root, controller):
        self.controller = controller

        # Layout
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label_nome = tk.Label(self.frame, text="Nome do Produto:")
        self.label_nome.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)

        self.label_preco = tk.Label(self.frame, text="Preço do Produto:")
        self.label_preco.grid(row=1, column=0)
        self.preco_entry = tk.Entry(self.frame)
        self.preco_entry.grid(row=1, column=1)

        self.cadastrar_button = tk.Button(self.frame, text="Cadastrar Produto", command=self.cadastrar_produto)
        self.cadastrar_button.grid(row=2, columnspan=2)

    def cadastrar_produto(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        self.controller.cadastrar_produto(nome, preco)
