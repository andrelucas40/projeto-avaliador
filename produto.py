from models.database import get_db_connection

class Produto:
    def __init__(self, id=None, nome=None, descricao=None, preco=None, estoque=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    @staticmethod
    def get_all():
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        connection.close()
        return produtos

    @staticmethod
    def add(nome, descricao, preco, estoque):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)",
                       (nome, descricao, preco, estoque))
        connection.commit()
        cursor.close()
        connection.close()

    # Métodos para editar, excluir, etc.
