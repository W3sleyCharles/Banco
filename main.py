# Estrutura do menu principal
menu_principal = """
1 - Criar Conta
2 - Acessar Conta
3 - Sair

=> """

# Estrutura do menu da conta
menu_conta = """
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

=> """

# Lista para armazenar as contas
contas = []

# Função para criar uma nova conta
def criar_conta():
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    for conta in contas:
        if conta["cpf"] == cpf:
            print("Erro: Já existe uma conta com esse CPF.")
            return
    nova_conta = {
        "cpf": cpf,
        "nome": nome,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0,
        "limite_saques": 3
    }
    contas.append(nova_conta)
    print("Conta criada com sucesso!")

# Função para acessar uma conta existente
def acessar_conta():
    cpf = input("Informe o CPF da conta: ")
    for conta in contas:
        if conta["cpf"] == cpf:
            print(f"Bem-vindo(a), {conta['nome']}!")
            return conta
    print("Erro: Conta não encontrada.")
    return None

# Função para exibir o menu da conta
def menu_da_conta(conta):
    while True:
        opcao = input(menu_conta)

        # Opção de depósito
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")

        # Opção de saque
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > conta["saldo"]
            excedeu_limite = valor > conta["limite"]
            excedeu_saques = conta["numero_saques"] >= conta["limite_saques"]

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                conta["saldo"] -= valor
                conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
                conta["numero_saques"] += 1
            else:
                print("Operação falhou! O valor informado é inválido.")

        # Opção de extrato
        elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            print("==========================================")

        # Opção de sair
        elif opcao == "4":
            break

        # Caso a opção informada seja inválida
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Loop principal do sistema
while True:
    opcao_principal = input(menu_principal)

    # Opção para criar uma nova conta
    if opcao_principal == "1":
        criar_conta()

    # Opção para acessar uma conta existente
    elif opcao_principal == "2":
        conta = acessar_conta()
        if conta:
            menu_da_conta(conta)

    # Opção para sair do sistema
    elif opcao_principal == "3":
        break

    # Caso a opção informada seja inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
