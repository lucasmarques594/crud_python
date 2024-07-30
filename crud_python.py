import mysql.connector

# Função para criar a tabela de usuários
def criar_tabela():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='crud'
    )
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nome VARCHAR(255) NOT NULL,
                   idade INT)''')
    conexao.commit()
    conexao.close()

# Função para adicionar um novo usuário C
def adicionar_usuario(nome, idade):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='crud'
    )
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (%s, %s)''', (nome, idade))
    conexao.commit()
    conexao.close()

# Função para listar todos os usuários R
def lista_usuarios():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='crud'
    )
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

# Função para atualizar um usuário existente U
def atualizar_usuario(id, nome, idade):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='crud'
    )
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = %s, idade = %s WHERE id = %s''', (nome, idade, id))
    conexao.commit()
    conexao.close()

# Função para deletar um usuário D
def deletar_usuario(id):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='crud'
    )
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = %s''', (id,))
    conexao.commit()
    conexao.close()

# Função para exibir o menu
def menu():
    print("\n1. Adicionar usuário")
    print('2. Listar usuários')
    print('3. Atualizar usuário')
    print('4. Deletar usuário')
    print('5. Sair')

# Criação da tabela no início
criar_tabela()

# Loop principal do programa
while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        nome = input('Digite o nome do usuário: ')
        idade = int(input('Digite a idade do usuário: '))
        adicionar_usuario(nome, idade)
        print('Usuário adicionado com sucesso!')
    elif escolha == '2':
        print('\nTodos os usuários: ')
        lista_usuarios()
    elif escolha == '3':
        id = int(input('Digite o ID do usuário a ser atualizado: '))
        nome = input('Digite o novo nome do usuário: ')
        idade = int(input('Digite a nova idade do usuário: '))
        atualizar_usuario(id, nome, idade)
        print('Usuário atualizado com sucesso!')
    elif escolha == '4':
        id = int(input('Digite o ID do usuário a ser deletado: '))
        deletar_usuario(id)
        print('Usuário deletado com sucesso!')
    elif escolha == '5':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
