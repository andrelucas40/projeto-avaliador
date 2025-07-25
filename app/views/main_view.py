import tkinter as tk
from tkinter import messagebox
from app.controllers.produto_controller import ProdutoController

class MainView:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Controle de Loja")

        # Botão para abrir a janela de produtos
        self.btn_produtos = tk.Button(master, text="Produtos", command=self.open_produtos)
        self.btn_produtos.pack()

    def open_produtos(self):
        self.produtos_view = ProdutosView(self.master)

class ProdutosView:
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Cadastro de Produtos")

        self.controller = ProdutoController()

        # Listar produtos
        self.list_produtos()

    def list_produtos(self):
        produtos = self.controller.get_all_produtos()
        for produto in produtos:
            print(produto)  # Aqui você pode exibir na tela
