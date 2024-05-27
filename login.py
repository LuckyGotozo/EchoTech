import webbrowser
import os

usuarios = {
    "guilherme": "123"
}

def verificar_login(username, password):
    if username in usuarios and usuarios[username] == password:
        return True
    else:
        return False

def pagina_inicial():
    caminho_para_html = 'login.html'
    if os.path.exists(caminho_para_html):
        webbrowser.open('file://' + os.path.realpath(caminho_para_html))
    else:
        print("Arquivo HTML não encontrado!")

def pagina_secundaria():
    print("Bem-vindo à página secundária!")

def redefinir_senha(username, new_password):
    if username in usuarios:
        usuarios[username] = new_password
        print(f"A senha para o usuário {username} foi redefinida com sucesso.")
    else:
        print("Usuário não encontrado.")

def adicionar_usuario(username, password):
    if username not in usuarios:
        usuarios[username] = password
        print(f"Usuário {username} adicionado com sucesso.")
    else:
        print("Usuário já existe.")

def autenticacao():
    while True:
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")

        if verificar_login(username, password):
            pagina_inicial()
            return True
        else:
            print("Credenciais inválidas. Tente novamente.")
            opcao = input("Deseja redefinir a senha ou adicionar um novo usuário? (redefinir/adicionar/nenhum): ")
            if opcao.lower() == "redefinir":
                nova_senha = input("Digite a nova senha: ")
                redefinir_senha(username, nova_senha)
                print("Tente fazer login novamente com a nova senha.")
                return False
            elif opcao.lower() == "adicionar":
                novo_usuario = input("Digite o nome de usuário para o novo usuário: ")
                nova_senha = input("Digite a senha para o novo usuário: ")
                adicionar_usuario(novo_usuario, nova_senha)
                return False

if __name__ == "__main__":
    logged_in = False
    while not logged_in:
        logged_in = autenticacao()