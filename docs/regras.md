# 📏 Regras do Projeto — Controle de Estoque API

## 🎯 Objetivo
Manter o projeto organizado, funcional e sem conflitos entre os desenvolvedores.

---

## 🧠 Padrão Geral

- Utilizar **Python com Flask**
- Trabalhar com **JSON** nas requisições e respostas
- Código simples, limpo e funcional (não complicar)
- **NÃO usar banco de dados**
- Armazenamento dos dados em memória (listas mockadas/hardcoded)

---

## 📁 Estrutura do Projeto (OBRIGATÓRIO)

NÃO criar arquivos fora dessa estrutura:

controle-estoque/
├── app.py
├── models/
├── routes/

---

## 👨‍💻 Responsabilidades

- **MARI** → `models/` (classes Produto, Entrada e Saida)
- **MARCOS** → `routes/` (endpoints da API)
- **ERICK** → lógica + integração + testes
- (Jordan) → integração final + organização

---

## 🚫 Regras Importantes

- ❌ NÃO modificar o arquivo `app.py` sem autorização do Tech Lead
- ❌ NÃO criar arquivos fora da estrutura definida
- ❌ NÃO mudar nomes de classes ou rotas sem avisar
- ❌ NÃO subir código quebrado

---

## 📌 Padrão de Código

- Usar nomes em **português**
  - `Produto`, `Entrada`, `Saida`
  - `/produtos`, `/entradas`, `/saidas`

- Manter consistência:
  - mesmo padrão de indentação
  - nomes claros

---

## 🔗 API (Padrão obrigatório)

### Produtos
- GET /produtos
- POST /produtos

### Entradas
- GET /entradas
- POST /entradas

### Saídas
- GET /saidas
- POST /saidas

---

## 🧪 Testes

- Utilizar **Postman**
- Testar TODOS os endpoints antes de finalizar
- Garantir que a API responde corretamente

---

## 🔄 Versionamento (Git)

- Cada dev deve:
  - Fazer commits organizados
  - Não sobrescrever código dos outros
  - Sempre puxar atualizações antes de enviar (`git pull`)

---

## ⚠️ Regra de Ouro

Se tiver dúvida ou algo não estiver funcionando:
👉 Falar com o Tech Lead antes de alterar qualquer coisa

---

## 🏆 Objetivo Final

Sistema simples, funcionando e bem organizado.

> Melhor um sistema simples funcionando do que algo complexo quebrado.