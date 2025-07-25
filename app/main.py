import tkinter as tk
from app.views.produto_view import ProdutoView
from app.views.cliente_view import ClienteView
from app.controllers.produto_controller import ProdutoController
from app.controllers.cliente_controller import ClienteController

def main():
    root = tk.Tk()
    root.title("Sistema de Controle de Loja")       

    produto_controller = ProdutoController()
    produto_view = ProdutoView(root, produto_controller)

    cliente_controller = ClienteController()
    cliente_view = ClienteView(root, cliente_controller)

    root.mainloop()

if __name__ == "__main__":
    main()
