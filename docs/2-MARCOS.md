# MARCOS - API (Flask)

## Objetivo
Responsável por criar os endpoints da API utilizando Flask.

## Tarefas

- Criar rotas para manipular os dados:

### Produtos
- GET /produtos → listar todos os produtos
- POST /produtos → cadastrar um novo produto

### Entradas (Entrada de Estoque)
- GET /entradas → listar todas as entradas
- POST /entradas → registrar entrada de produto

### Saídas (Saída de Estoque)
- GET /saidas → listar todas as saídas
- POST /saidas → registrar saída de produto

## Requisitos

- Utilizar Flask
- Receber e retornar dados em JSON
- Conectar com as classes criadas (Produto, Entrada e Saida)

## Observações

- Não precisa implementar lógica complexa
- Focar em fazer a API funcionar corretamente

## Entregável

- Arquivo:
  - routes/routes.py