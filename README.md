Guia Rápido: CRUD de Usuários com XAMPP
Este aplicativo é um exemplo simples de CRUD (Create, Read, Update, Delete) para gerenciamento de usuários usando MySQL, e você pode executá-lo com o XAMPP. Aqui está uma visão geral rápida:

O Que É Um CRUD?
CRUD é um acrônimo para quatro operações básicas em bancos de dados:

Create: Adicionar novos registros.
Read: Ler e exibir registros existentes.
Update: Atualizar registros existentes.
Delete: Remover registros.
O Que o Código Faz?
Conexão com o Banco de Dados:

O código usa o módulo mysql.connector para se conectar ao MySQL, que deve estar rodando no XAMPP.
Funções CRUD:

Criar Tabela: Se a tabela usuarios não existir, ela é criada com colunas para id, nome e idade.
Adicionar Usuário: Insere um novo usuário com nome e idade na tabela.
Listar Usuários: Recupera e exibe todos os usuários na tabela.
Atualizar Usuário: Modifica o nome e a idade de um usuário existente, identificado pelo id.
Deletar Usuário: Remove um usuário da tabela baseado no id.
Menu de Interação:

O programa exibe um menu para escolher entre adicionar, listar, atualizar ou deletar usuários.
Como Configurar e Executar
Instalação do XAMPP:

Baixe e instale o XAMPP. Inicie o Apache e o MySQL no painel de controle do XAMPP.
Preparação do Banco de Dados:

Acesse phpMyAdmin através do XAMPP e crie um banco de dados chamado crud.
Instalação do MySQL Connector:

Instale o pacote mysql-connector-python usando o comando:
sh
Copiar código
pip install mysql-connector-python
Execução do Código:

Salve o código em um arquivo Python e execute-o. O aplicativo exibirá um menu para gerenciar usuários.
Estarei disponível para responder suas perguntas e ajudar com o que for necessário. Se precisar de mais detalhes ou suporte adicional, não hesite em entrar em contato!
