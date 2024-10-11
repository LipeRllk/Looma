import psycopg2
from psycopg2 import sql

# Classe responsável pela interação com o banco de dados
class Database:
    
    # Inicializa a classe Database e faz a conexão com o banco de dados PostgreSQL
    def __init__(self):
        # Conecta ao banco de dados usando as informações fornecidas
        self.connection = psycopg2.connect(
            host="localhost",      # Endereço do banco de dados (neste caso, o banco está no próprio computador)
            database="looma",      # Nome do banco de dados
            user="postgres",       # Usuário do banco de dados
            password="1234"        # Senha do banco de dados
        )
        # Cria um cursor para executar comandos SQL no banco de dados
        self.cursor = self.connection.cursor()

    # Método para criar um novo usuário no banco de dados
    def create_user(self, name, email, password):
        try:
            # Executa um comando SQL para inserir um novo usuário na tabela 'users'
            self.cursor.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
                RETURNING id;  # Retorna o ID do usuário que acabou de ser criado
                """, (name, email, password)
            )
            # Pega o ID do novo usuário criado
            user_id = self.cursor.fetchone()[0]
            # Confirma as mudanças no banco de dados (salva as alterações)
            self.connection.commit()
            return user_id  # Retorna o ID do novo usuário
        except psycopg2.Error as e:
            # Exibe uma mensagem de erro caso ocorra algum problema na criação do usuário
            print(f"Error creating user: {e}")
            # Desfaz qualquer alteração no banco de dados em caso de erro
            self.connection.rollback()

    # Método para buscar um usuário pelo email no banco de dados
    def get_user(self, email):
        # Executa um comando SQL para buscar um usuário pelo email
        self.cursor.execute(
            """
            SELECT * FROM users WHERE email = %s;
            """, (email,)
        )
        # Retorna os dados do usuário encontrado ou None se não encontrar
        return self.cursor.fetchone()

    # Método para fechar a conexão com o banco de dados
    def close(self):
        # Fecha o cursor (não podemos mais executar comandos SQL depois disso)
        self.cursor.close()
        # Fecha a conexão com o banco de dados
        self.connection.close()
