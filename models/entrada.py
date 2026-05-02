class Entrada:
    def __init__(self, id, produto_id, quantidade, data, fornecedor):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data = data
        self.fornecedor = fornecedor

    def to_dict(self):
        return {
            "id": self.id,
            "produto_id": self.produto_id,
            "quantidade": self.quantidade,
            "data": self.data,
            "fornecedor": self.fornecedor
        }