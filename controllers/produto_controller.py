from models.produto import Produto

class ProdutoController:
    def __init__(self):
        self.produto_model = Produto

    def get_all_produtos(self):
        return self.produto_model.get_all()

    def add_produto(self, nome, descricao, preco, estoque):
        self.produto_model.add(nome, descricao, preco, estoque)
