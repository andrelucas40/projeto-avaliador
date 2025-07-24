import tkinter as tk
from views.produto_view import ProdutoView
from views.cliente_view import ClienteView
from views.venda_view import VendaView
from controllers.produto_controller import ProdutoController
from controllers.cliente_controller import ClienteController
from controllers.venda_controller import VendaController

def main():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Sistema de Controle de Loja")

    # Inicializa os controladores
    produto_controller = ProdutoController()
    cliente_controller = ClienteController()
    venda_controller = VendaController()

    # Inicializa as views
    produto_view = ProdutoView(root, produto_controller)
    cliente_view = ClienteView(root, cliente_controller)
    venda_view = VendaView(root, venda_controller)

    # Organiza as views na janela principal (pode usar abas, botões ou um layout mais complexo)
    produto_view.pack(side="left", padx=10, pady=10)
    cliente_view.pack(side="left", padx=10, pady=10)
    venda_view.pack(side="left", padx=10, pady=10)

    # Inicia o loop do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
