# 📚 Biblioteca API

Uma API REST simples para gerenciamento de livros e empréstimos desenvolvida com Python e Flask.

## 🎯 Objetivo

Sistema simples e funcional para gerenciar livros e empréstimos em uma biblioteca, com foco em organização e facilidade de uso.

## 🛠️ Stack Tecnológico

- **Python** - Linguagem principal
- **Flask** - Framework web
- **JSON** - Formato de dados para requisições e respostas

## 📁 Estrutura do Projeto

```
livros_e_emprestimos/
├── app.py              # Aplicação principal
├── models/             # Classes de dados
│   ├── livro.py        # Classe Livro
│   └── emprestimo.py   # Classe Emprestimo
├── routes/             # Endpoints da API
│   └── routes.py       # Definição das rotas
├── tarefas/            # Documentação do projeto
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/JORD4N-01/livros_e_emprestimos
cd livros_e_emprestimos
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## 📡 Endpoints da API

### Livros

- `GET /livros` - Lista todos os livros
- `POST /livros` - Adiciona um novo livro

### Empréstimos

- `GET /emprestimos` - Lista todos os empréstimos
- `POST /emprestimos` - Realiza um novo empréstimo

## 🧪 Testes

Recomendamos usar o **Postman** para testar os endpoints:

1. Importe a coleção de testes (se disponível)
2. Configure as requisições para `http://localhost:5000`
3. Teste todos os endpoints para garantir funcionamento

## 📝 Exemplos de Uso

### Adicionar um Livro

```json
POST /livros
Content-Type: application/json

{
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "isbn": "978-85-5941-128-6"
}
```

### Realizar Empréstimo

```json
POST /emprestimos
Content-Type: application/json

{
    "livro_id": 1,
    "pessoa": "João Silva",
    "data_emprestimo": "2024-01-15"
}
```

## 🔧 Desenvolvimento

### Padrões do Projeto

- Código em português (classes e endpoints)
- Estrutura obrigatória de diretórios
- Commits organizados
- Testes obrigatórios antes de finalizar

### Equipe

- **MARI** → Models (classes Livro e Emprestimo)
- **MARCOS** → Routes (endpoints da API)
- **ERICK** → Lógica + Integração + Testes
- **Jordan** → Integração final + organização

## 📋 Regras Importantes

- ❌ Não modificar `app.py` sem autorização
- ❌ Não criar arquivos fora da estrutura definida
- ❌ Não mudar nomes de classes ou rotas sem avisar
- ❌ Não subir código quebrado

## 🏆 Objetivo Final

Sistema simples, funcionando e bem organizado.

> "Melhor um sistema simples funcionando do que algo complexo quebrado."