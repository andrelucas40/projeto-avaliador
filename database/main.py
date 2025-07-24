import tkinter as tk
from views.produto_view import ProdutoView
from controllers.produto_controller import ProdutoController

def main():
    root = tk.Tk()
    root.title("Sistema de Controle de Loja")

    produto_controller = ProdutoController()
    produto_view = ProdutoView(root, produto_controller)

    root.mainloop()

if __name__ == "__main__":
    main()
