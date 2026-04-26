# 📏 Regras do Projeto — Biblioteca API

## 🎯 Objetivo
Manter o projeto organizado, funcional e sem conflitos entre os desenvolvedores.

---

## 🧠 Padrão Geral

- Utilizar **Python com Flask**
- Trabalhar com **JSON** nas requisições e respostas
- Código simples, limpo e funcional (não complicar)

---

## 📁 Estrutura do Projeto (OBRIGATÓRIO)

NÃO criar arquivos fora dessa estrutura:

biblioteca-api/
├── app.py
├── models/
├── routes/

---

## 👨‍💻 Responsabilidades

- **MARI** → `models/` (classes Livro e Emprestimo)
- **MARCOS** → `routes/` (endpoints da API)
- **Dev 3** → lógica + integração + testes
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
  - `Livro`, `Emprestimo`
  - `/livros`, `/emprestimos`

- Manter consistência:
  - mesmo padrão de indentação
  - nomes claros

---

## 🔗 API (Padrão obrigatório)

### Livros
- GET /livros
- POST /livros

### Empréstimos
- GET /emprestimos
- POST /emprestimos

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