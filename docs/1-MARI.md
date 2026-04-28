# MARI - Modelagem (POO)

## Objetivo
Responsável por criar a base do sistema utilizando Programação Orientada a Objetos (POO).

## Tarefas

- Criar a classe `Produto`
  - Atributos:
    - id
    - nome
    - descricao
    - preco
    - quantidade_estoque

- Criar a classe `Entrada`
  - Atributos:
    - id
    - produto_id
    - quantidade
    - data
    - fornecedor

- Criar a classe `Saida`
  - Atributos:
    - id
    - produto_id
    - quantidade
    - data
    - cliente

- Definir os relacionamentos:
  - Uma entrada deve estar ligada a um produto
  - Uma saída deve estar ligada a um produto

## Observações

- O código deve ser simples e organizado
- Não precisa usar banco de dados, apenas estrutura de classes
- Manter padrão de nomes definido pelo Tech Lead

## Entregável

- Arquivos:
  - models/produto.py
  - models/entrada.py
  - models/saida.py