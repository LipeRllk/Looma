from authModule import Auth

# Função principal que lida com o fluxo do programa
def main():
    # Cria uma instância da classe Auth para gerenciar a autenticação de usuários
    auth = Auth()

    # Exibe as opções para o usuário: Registrar ou Login
    print("1. Registrar")
    print("2. Login")
    
    # Solicita que o usuário escolha uma das opções
    choice = input("Escolha uma opção: ")

    # Se o usuário escolher a opção 1 (Registrar)
    if choice == '1':
        # Solicita o nome, email e senha do usuário
        name = input("Digite o seu nome: ")
        email = input("Digite o seu e-mail: ")
        password = input("Crie uma senha: ")
        # Chama o método para registrar o usuário com os dados fornecidos
        auth.register_user(name, email, password)

    # Se o usuário escolher a opção 2 (Login)
    elif choice == '2':
        # Solicita o email e a senha para realizar o login
        email = input("Digite o seu e-mail: ")
        password = input("Digite a sua senha: ")
        # Chama o método para realizar o login com os dados fornecidos
        auth.login_user(email, password)

    # Fecha a conexão com o banco de dados quando o programa termina
    auth.close_connection()

# Verifica se o script está sendo executado diretamente (não importado) e chama a função main
if __name__ == "__main__":
    main()
