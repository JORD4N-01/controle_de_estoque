# ERICK - Lógica + Integração + Testes

## Objetivo
Responsável por integrar o sistema e garantir que tudo funcione corretamente.

## Tarefas

- Criar armazenamento em memória:
  - Lista de produtos
  - Lista de entradas
  - Lista de saídas

- Implementar regras básicas:
  - Verificar se o produto existe antes de registrar entrada/saída
  - Atualizar quantidade em estoque ao registrar entrada (aumenta)
  - Atualizar quantidade em estoque ao registrar saída (diminui)
  - Verificar se há estoque suficiente antes de permitir saída
  - Evitar dados inválidos

- Integrar:
  - Classes (models)
  - Rotas (API)

## Testes

- Utilizar Postman para testar:
  - GET /produtos
  - POST /produtos
  - GET /entradas
  - POST /entradas
  - GET /saidas
  - POST /saidas

- Garantir que:
  - API responde corretamente
  - Quantidade em estoque é atualizada corretamente
  - Não é permitido saída sem estoque suficiente
  - Não há erros

## Observações

- Essa função é crítica para a apresentação
- Se algo quebrar, é aqui que resolve

## Entregável

- Sistema funcionando integrado
- Testes realizados no Postman