import psycopg2
from psycopg2 import sql

# Classe responsável pela interação com o banco de dados
class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="looma",
            user="postgres",
            password="1234"
        )
        self.cursor = self.connection.cursor()

    def create_user(self, name, email, password):
        try:
            self.cursor.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
                RETURNING id;
                """, (name, email, password)
            )
            user_id = self.cursor.fetchone()[0]
            self.connection.commit()
            return user_id
        except psycopg2.Error as e:
            print(f"Error creating user: {e}")
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
