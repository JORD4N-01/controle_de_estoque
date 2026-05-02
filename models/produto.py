class Produto:
    def __init__(self, id, nome, descricao, preco, quantidade_estoque):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "quantidade_estoque": self.quantidade_estoque 
        }

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            return "Quantidade insuficiente"
        self.quantidade_estoque -= quantidade