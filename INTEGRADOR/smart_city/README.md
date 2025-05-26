📡 Smart City
Este projeto faz parte do curso técnico de Desenvolvimento de Sistemas do SENAI “Roberto Mange” e tem como objetivo criar uma aplicação de monitoramento de sensores para uma cidade inteligente. Os dados dos sensores são simulados e disponibilizados via API RESTful desenvolvida com Django Rest Framework e consumida por um front-end em React.

🚀 Objetivo
Desenvolver um back-end com Django Rest Framework para gerenciar e expor dados de sensores (temperatura, luminosidade, umidade e contador) e disponibilizá-los para o front-end em React, com autenticação JWT para garantir a segurança dos endpoints.

🛠️ Funcionalidades
✅ CRUD de sensores e ambientes (criar, ler, atualizar, deletar)<br>
✅ Relacionamento entre tabelas (conforme diagrama do projeto)<br>
✅ Filtros e localização de dados por sensor, data e status<br>
✅ Atualização de status do sensor (ativo, inativo)<br>
✅ Importação de dados de planilhas (.xlsx) para o banco<br>
✅ Exportação de dados em planilhas<br>
✅ Autenticação JWT<br>
✅ Simulação de dados para testes

📂 Estrutura de Pastas
bash
Copiar
Editar
smart_city/
├── back/
│   ├── api_smart/
│   │   ├── management/commands/      # Scripts para importar dados das planilhas
│   │   ├── migrations/               # Migrations do Django
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                 # Modelos de dados dos sensores
│   │   ├── serializers.py            # Serializers para a API
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py                  # Views com endpoints da API
│   │   ├── import_xlsx.py            # Script de importação de planilhas
│   │   ├── <dados>.xlsx              # Planilhas de dados de sensores e ambientes
│   ├── smart_city/                   # Configurações do projeto Django
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py               # Configuração principal
│   │   ├── urls.py                   # Rotas principais
│   │   ├── wsgi.py
│   ├── manage.py
│   ├── requirements.txt              # Dependências do projeto
├── front/                            # Aplicação front-end em React
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── api.jsx
│   ├── eslint.config.js
│   ├── ...
├── .gitignore
├── env/                              # Ambiente virtual Python
└── README.md                         # Este arquivo
💾 Banco de Dados
O projeto utiliza o MySQL como banco de dados, gerenciado via MySQL Workbench. As configurações de conexão estão definidas no arquivo settings.py do Django, utilizando as variáveis de ambiente para maior segurança e flexibilidade.

🔐 Autenticação
A autenticação é feita através de JSON Web Tokens (JWT). Para acessar os endpoints protegidos, é necessário incluir o token no cabeçalho das requisições.

📦 Como executar o projeto
1️⃣ Clone o repositório:

bash
Copiar
Editar
git clone <URL-do-repositório>
cd smart_city
2️⃣ Crie e ative o ambiente virtual:

bash
Copiar
Editar
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
3️⃣ Instale as dependências:

bash
Copiar
Editar
pip install -r back/requirements.txt
4️⃣ Configure o banco de dados MySQL no arquivo back/smart_city/settings.py:

python
Copiar
Editar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smart_city_db',
        'USER': 'root',  # seu usuário do MySQL
        'PASSWORD': 'sua_senha',  # sua senha do MySQL
        'HOST': 'localhost',      # ou o IP/hostname do servidor MySQL
        'PORT': '3306',           # porta padrão do MySQL
    }
}
5️⃣ Rode as migrações do banco de dados:

bash
Copiar
Editar
cd back
python manage.py makemigrations
python manage.py migrate
6️⃣ Crie um superusuário (conforme instruções):

bash
Copiar
Editar
python manage.py createsuperuser
# username = <seu primeiro nome, sem acentuação>
# password = <seu número de matrícula no senai>
7️⃣ Importe os dados das planilhas (opcional):

bash
Copiar
Editar
python manage.py import_xlsx  # Ou o comando customizado específico
8️⃣ Inicie o servidor:

bash
Copiar
Editar
python manage.py runserver
9️⃣ Acesse o front-end React no diretório front e rode:

bash
Copiar
Editar
cd front
npm install
npm run dev
🧩 Metodologia Scrum
O desenvolvimento foi organizado utilizando Scrum, com os seguintes papéis:

Product Owner: Instrutor

Scrum Master: Aluno designado ou instrutor

Equipe de Desenvolvimento: Alunos

Artefatos e eventos do Scrum incluíram:

Product Backlog

Sprint Backlog

Incremento

Sprint Planning, Daily Scrum, Sprint Review e Sprint Retrospective

📋 Tarefas Realizadas
Configuração do projeto Django e do DRF

Modelagem e criação do banco de dados (MySQL via Workbench)

Implementação dos endpoints da API (CRUD)

Implementação de autenticação JWT

Scripts para importação de dados das planilhas

Integração com front-end React para exibir e gerenciar os dados dos sensores

📑 Licença
Projeto acadêmico desenvolvido para fins de aprendizado no SENAI “Roberto Mange”.

✏️ Observações
Para o login do superusuário, utilize seu primeiro nome (sem acento) e o número de matrícula como senha, conforme exigido pelo projeto.

Os dados dos sensores são simulados durante a fase de testes.

O banco de dados utilizado é o MySQL via Workbench, configurado para suportar múltiplos usuários e facilitar a manutenção.