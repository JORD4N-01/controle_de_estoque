from flask import Blueprint, jsonify, request

from models.entrada import Entrada
from models.produto import Produto
from models.saida import Saida

routes_bp = Blueprint("routes", __name__)

# ======================
# MOCK DATA (em memória)
# ======================
produtos = []
entradas = []
saidas = []


def _json_body():
    return request.get_json(silent=True) or {}


def _find_produto(produto_id: int):
    for produto in produtos:
        if produto.id == produto_id:
            return produto
    return None


# ======================
# PRODUTOS
# ======================


@routes_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify([p.to_dict() for p in produtos])


@routes_bp.route("/produtos", methods=["POST"])
def criar_produto():
    data = _json_body()

    nome = data.get("nome")
    quantidade = data.get("quantidade", 0)

    if not nome:
        return jsonify({"erro": "Campo 'nome' é obrigatório"}), 400

    try:
        quantidade = int(quantidade)
    except (TypeError, ValueError):
        return jsonify({"erro": "Campo 'quantidade' deve ser um número"}), 400

    if quantidade < 0:
        return jsonify({"erro": "Campo 'quantidade' não pode ser negativo"}), 400

    produto = Produto(id=len(produtos) + 1, nome=nome, quantidade=quantidade)
    produtos.append(produto)
    return jsonify(produto.to_dict()), 201


# ======================
# ENTRADAS
# ======================


@routes_bp.route("/entradas", methods=["GET"])
def listar_entradas():
    return jsonify([e.to_dict() for e in entradas])


@routes_bp.route("/entradas", methods=["POST"])
def registrar_entrada():
    data = _json_body()

    try:
        produto_id = int(data.get("produto_id"))
        quantidade = int(data.get("quantidade"))
    except (TypeError, ValueError):
        return jsonify({"erro": "Campos 'produto_id' e 'quantidade' devem ser números"}), 400

    if quantidade <= 0:
        return jsonify({"erro": "Campo 'quantidade' deve ser maior que zero"}), 400

    produto = _find_produto(produto_id)
    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404

    produto.adicionar_estoque(quantidade)

    entrada = Entrada(
        id=len(entradas) + 1,
        produto_id=produto_id,
        quantidade=quantidade,
        data=data.get("data"),
        fornecedor=data.get("fornecedor"),
    )
    entradas.append(entrada)
    return jsonify(entrada.to_dict()), 201


# ======================
# SAÍDAS
# ======================


@routes_bp.route("/saidas", methods=["GET"])
def listar_saidas():
    return jsonify([s.to_dict() for s in saidas])


@routes_bp.route("/saidas", methods=["POST"])
def registrar_saida():
    data = _json_body()

    try:
        produto_id = int(data.get("produto_id"))
        quantidade = int(data.get("quantidade"))
    except (TypeError, ValueError):
        return jsonify({"erro": "Campos 'produto_id' e 'quantidade' devem ser números"}), 400

    if quantidade <= 0:
        return jsonify({"erro": "Campo 'quantidade' deve ser maior que zero"}), 400

    produto = _find_produto(produto_id)
    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404

    result = produto.remover_estoque(quantidade)
    if result == "Quantidade insuficiente":
        return jsonify({"erro": "Estoque insuficiente"}), 400

    saida = Saida(
        id=len(saidas) + 1,
        produto_id=produto_id,
        quantidade=quantidade,
        data=data.get("data"),
        cliente=data.get("cliente"),
    )
    saidas.append(saida)
    return jsonify(saida.to_dict()), 201


def register_routes(app):
    app.register_blueprint(routes_bp)