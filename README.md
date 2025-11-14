📦 Projeto Final
 ┣ 📂 back-end
 ┃ ┣ 📂 __pycache__
 ┃ ┣ 📜 conexao.py      # Arquivo responsável pela conexão com o banco de dados
 ┃ ┣ 📜 funcao.py       # Funções utilizadas pelo sistema
 ┃ ┗ 📜 main.py         # Executa o back-end
 ┣ 📂 front-end
 ┃ ┗ 📜 app.py          # Arquivo principal da interface/front-end
 ┣ 📜 .env              # Variáveis de ambiente (senhas, configs sensíveis)
 ┣ 📜 .gitignore        # Arquivos ignorados pelo Git
 ┗ 📜 README.md         # Documentação do projeto
  


🚀 Tecnologias Utilizadas

BACK-END

- FastAPI

- Psycopg2

- PostgreSQL

- Python-dotenv

FRONT-END

- Streamlit

- Requests



*Instalar dependência

 pip install fastapi uvicorn psycopg2 python-dotenv streamlit requests




🔑 Configuração do arquivo .env

DB_NAME=nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432




*Banco de Dados

criar_tabela()

Campo	     Tipo	       Descrição
id	         SERIAL	       Chave primária
nome	     TEXT   	   Nome do produto
categoria    TEXT	       Categoria do produto
preco	     REAL	       Preço
quantidade   INTEGER	   Quantidade em estoque





🧠 Funcionalidades (CRUD)

✔ Criar produtos
✔ Listar produtos
✔ Atualizar quantidade
✔ Deletar produtos
✔ Buscar produto pelo ID

Tudo isso via funções do arquivo funcao.py.





📡 Rotas da API (FastAPI)

GET /

Retorna mensagem de boas-vindas.

GET /produtos

Lista todos os produtos cadastrados.

POST /produtos

*Adiciona um produto.
Parâmetros (query):

- nome

- categoria

- preco

- quantidade

DELETE /produtos/{id}

Remove produto pelo ID.

PUT /produtos/id

Atualiza a quantidade de um produto.
Parâmetros:

- id

- quantidade




▶️Como Rodar o Back-end (API)

uvicorn back-end.main:app --reload

A API abrirá em:

👉 http://127.0.0.1:8000





💻 Como Rodar o Front-end (Streamlit)

python -m streamlit run front-end/app.py





🖥️ Interface (Streamlit)

A interface contém:

🔍 Catálogo de produtos

Tabela com todos os produtos cadastrados.

➕ Cadastrar produto

Formulário de inclusão.

❌ Deletar produto

Remove produtos pelo ID.

Totalmente integrado com a API FastAPI.