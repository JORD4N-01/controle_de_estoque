from flask import Blueprint, request, jsonify
from models.produto import Produto
from models.entrada import Entrada
from models.saida import Saida

routes_bp = Blueprint('routes', __name__)

# ======================
# MOCK DATA (em memória)
# ======================
produtos = []
entradas = []
saidas = []

# ======================
# PRODUTOS
# ======================

@routes_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify([p.to_dict() for p in produtos])


@routes_bp.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.json

    # Criando produto baseado no README
    produto = Produto(
        id=len(produtos) + 1,
        nome=data.get('nome'),
        descricao=data.get('descricao'),
        preco=data.get('preco'),
        quantidade_estoque=data.get('quantidade_estoque', 0)
    )

    produtos.append(produto)

    return jsonify(produto.to_dict()), 201


# ======================
# ENTRADAS
# ======================

@routes_bp.route('/entradas', methods=['GET'])
def listar_entradas():
    return jsonify([e.to_dict() for e in entradas])


@routes_bp.route('/entradas', methods=['POST'])
def registrar_entrada():
    data = request.json

    for p in produtos:
        if p.get_id() == data.get('produto_id'):

            # Atualiza estoque
            nova_qtd = p.get_quantidade_estoque() + data.get('quantidade', 0)
            p.set_quantidade_estoque(nova_qtd)

            entrada = Entrada(
                produto_id=data.get('produto_id'),
                quantidade=data.get('quantidade'),
                data=data.get('data'),
                fornecedor=data.get('fornecedor')
            )

            entradas.append(entrada)

            return jsonify(entrada.to_dict()), 201

    return jsonify({"erro": "Produto não encontrado"}), 404


# ======================
# SAÍDAS
# ======================

@routes_bp.route('/saidas', methods=['GET'])
def listar_saidas():
    return jsonify([s.to_dict() for s in saidas])


@routes_bp.route('/saidas', methods=['POST'])
def registrar_saida():
    data = request.json

    for p in produtos:
        if p.get_id() == data.get('produto_id'):

            if p.get_quantidade_estoque() >= data.get('quantidade', 0):

                # Atualiza estoque
                nova_qtd = p.get_quantidade_estoque() - data.get('quantidade')
                p.set_quantidade_estoque(nova_qtd)

                saida = Saida(
                    produto_id=data.get('produto_id'),
                    quantidade=data.get('quantidade'),
                    data=data.get('data'),
                    cliente=data.get('cliente')
                )

                saidas.append(saida)

                return jsonify(saida.to_dict()), 201

            return jsonify({"erro": "Estoque insuficiente"}), 400

    return jsonify({"erro": "Produto não encontrado"}), 404