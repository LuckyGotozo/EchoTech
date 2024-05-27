user_data = {}
cart = []

def registrar_usuario():
    while True:
        username = input("Digite um nome de usuário: ")
        if username not in user_data:
            password = input("Digite uma senha: ")
            user_data[username] = {'password': password, 'budget': {}}
            print("Registro bem-sucedido!")
            return username
        else:
            print("Nome de usuário já em uso. Tente novamente.")

def login():
    while True:
        username = input("Digite seu nome de usuário: ")
        if username in user_data:
            password = input("Digite sua senha: ")
            if user_data[username]['password'] == password:
                print("Login bem-sucedido!")
                return username
            else:
                print("Senha incorreta. Tente novamente.")
        else:
            print("Nome de usuário não encontrado. Tente novamente.")

def criar_orcamento(username):
    orcamento = user_data[username]['budget']
    print("Criação de Orçamento")
    while len(orcamento) < 3:
        nome_produto = input(f"Digite o nome do produto: ")
        valor_produto = float(input(f"Digite o valor do produto: "))
        orcamento[nome_produto] = valor_produto
    print("Orçamento criado com sucesso!")

def adicionar_ao_carrinho(username):
    print("Produtos disponíveis:")
    orcamento = user_data[username]['budget']
    for produto, valor in orcamento.items():
        print(f"{produto}: R${valor}")
    while True:
        produto = input("Digite o nome do produto a ser adicionado ao carrinho (ou 'fim' para encerrar): ")
        if produto.lower() == 'fim':
            break
        if produto in orcamento:
            cart.append((username, produto, orcamento[produto]))
            print(f"{produto} adicionado ao carrinho de {username}!")

def calcular_valor_a_pagar(username):
    total = 0
    print("Produtos no carrinho:")
    for entry in cart:
        if entry[0] == username:
            print(f"{entry[1]}: R${entry[2]}")
            total += entry[2]

    print("\nOpções de pagamento:")
    print("1. À vista")
    print("2. Parcelado")
    option = input("Selecione uma opção de pagamento (1/2): ")

    if option == "1":
        print(f"Pagamento à vista confirmado para {username}!")
        print(f"Total a pagar: R${total}")
    elif option == "2":
        parcelas = int(input("Digite o número de parcelas: "))
        valor_parcela = total / parcelas
        print(f"Pagamento parcelado em {parcelas} vezes de R${valor_parcela} cada.")
        print(f"Total a pagar: R${total}")
    else:
        print("Opção de pagamento inválida. Tente novamente.")

while True:
    print("\nBem-vindo ao sistema de orçamento e pagamento")
    choice = input("Escolha uma opção:\n1. Registrar\n2. Login\n3. Sair\nOpção: ")

    if choice == "1":
        username = registrar_usuario()
    elif choice == "2":
        username = login()
        if username:
            criar_orcamento(username)
            adicionar_ao_carrinho(username)
            calcular_valor_a_pagar(username)
    elif choice == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
