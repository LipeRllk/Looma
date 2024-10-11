from dataBaseModule import Database
import hashlib

# Classe responsável pela autenticação de usuários
class Auth:
    
    # Inicializa a classe Auth, conectando com o banco de dados
    def __init__(self):
        self.db = Database()  # Cria uma conexão com o banco de dados usando a classe Database

    # Método para gerar uma senha segura com hash
    def hash_password(self, password):
        # Converte a senha em um hash SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    # Método para registrar um novo usuário no sistema
    def register_user(self, name, email, password):
        # Cria o hash (código) da senha para armazenamento seguro
        hashed_password = self.hash_password(password)
        # Tenta criar um novo usuário no banco de dados, retornando o ID do usuário criado
        user_id = self.db.create_user(name, email, hashed_password)
        
        # Verifica se o usuário foi criado com sucesso
        if user_id:
            print(f"Usuario {name} registrado com o ID {user_id}")  # Mensagem de sucesso
        else:
            print("Falha ao se registrar")  # Mensagem de erro

    # Método para fazer login de um usuário
    def login_user(self, email, password):
        # Busca o usuário pelo email no banco de dados
        user = self.db.get_user(email)
        
        # Verifica se o usuário existe
        if user:
            # Pega a senha armazenada (4 campo da tabela, índice 3)
            stored_password = user[3]
            
            # Compara a senha armazenada com o hash da senha que o usuário forneceu
            if stored_password == self.hash_password(password):
                print("Logado com sucesso")  # Mensagem de sucesso no login
                return user  # Retorna os dados do usuário logado
            else:
                print("Senha incorreta")  # Senha errada
        else:
            print("Usuario não encontrado")  # Email não encontrado no banco de dados

    # Método para fechar a conexão com o banco de dados
    def close_connection(self):
        self.db.close()  # Fecha a conexão com o banco de dados
