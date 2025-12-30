📌 TodoList

Uma aplicação To-Do List construída com Django (Python) que permite criar, buscar, editar e excluir tarefas. Este é um projeto web simples, ideal para aprendizagem de desenvolvimento Full Stack com Django e integração com autenticação de usuários.

🚀 Principais características

✔️ Cadastro e login de usuários
✔️ Criar novas tarefas
✔️ Buscar tarefas com filtro por título
✔️ Atualizar tarefa existente
✔️ Excluir tarefa
✔️ Layout responsivo e estilizado com HTML/CSS (tema dark)

🧰 Tecnologias utilizadas

O projeto foi desenvolvido com:
-Python
-Django
-SQLite (banco de dados local)
-HTML/CSS
-Templates Django

ESTRUTURA DO PROJETO:
├── accounts/           # App de autenticação de usuários
├── core/               # Lógica de tarefas e views
├── todolist/           # Configurações do Django
├── db.sqlite3          # Banco de dados local
├── manage.py           # Script principal do Django
├── templates/          # Templates HTML
└── static/             # Arquivos CSS e imagens

📥 Instalação e execução local

Clone o repositório:

git clone https://github.com/davinoroes/todolist.git


Acesse a pasta do projeto:

cd todolist


Crie um ambiente virtual (recomendado):

python -m venv venv


Ative o ambiente virtual:

Windows:

venv\Scripts\activate


Linux / MacOS:

source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Aplique as migrations:

python manage.py migrate


Execute o servidor:

python manage.py runserver


Abra o navegador em:

http://127.0.0.1:8000
