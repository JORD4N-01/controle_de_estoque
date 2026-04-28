# 🎤 Roteiro de Apresentação — Controle de Estoque API

## ⏱️ Tempo total: 10 minutos

## 🗣️ 1ª GABRIEL — Introdução

### Fala:
- Apresentar o tema:
  > "Nosso projeto é uma API de controle de estoque desenvolvida em Python utilizando Flask..."

- Explicar o objetivo:
  > "O objetivo é permitir o cadastro de produtos e o controle de entradas e saídas de estoque..."

- Problema resolvido:
  > "Centralizar e organizar o gerenciamento de produtos, rastreando movimentações de estoque de forma simples..."

---

## 🧩 2ª LOGAN — Modelagem

### Fala:
- Explicar POO:
  > "Utilizamos Programação Orientada a Objetos para estruturar o sistema..."

- Mostrar código:
  - Classe `Produto`
  - Classe `Entrada`
  - Classe `Saida`

- Explicar:
  - atributos
  - construtor (`__init__`)
  - relação entre as classes

---

## 🌐 3ª CAIO — API 

### Fala:
- Explicar API REST:
  > "Criamos uma API utilizando Flask para comunicação com o sistema..."

- Mostrar endpoints:
  - `GET /produtos`
  - `POST /produtos`
  - `GET /entradas`
  - `POST /entradas`
  - `GET /saidas`
  - `POST /saidas`

- Explicar:
  - uso de JSON
  - como os dados são enviados e recebidos

---

## ⚙️ 4ª VINICIUS — Lógica

### Fala:
- Explicar funcionamento interno:
  > "Utilizamos listas em memória para armazenar os dados..."

- Mostrar:
  - listas `produtos`, `entradas` e `saidas`
  - validação de estoque (verificar disponibilidade antes da saída)
  - atualização automática do estoque

- Explicar como:
  - dados são armazenados
  - estoque é atualizado ao registrar entrada/saída
  - dados são retornados pela API

---

## 🔄 5ªJORDAN — Integração + Testes (2–3 min)

### Fala:
- Explicar integração:
  > "Todas as partes foram integradas, conectando modelagem, API e lógica."

- Demonstrar no Postman:
  1. Criar produto
  2. Listar produtos
  3. Registrar entrada de estoque
  4. Registrar saída de estoque
  5. Verificar atualização do estoque

- Mostrar que:
  - sistema funciona
  - estoque é atualizado corretamente
  - dados fluem corretamente

---

- Falar de forma simples
- Não ler código inteiro
- Explicar o que o código FAZ
- Mostrar o sistema funcionando