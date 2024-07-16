menu = """
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

=> """

# Inicializando as variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do menu
while True:
    # Exibindo o menu e lendo a opção do usuário
    opcao = input(menu)

    # Opção de depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        # Verificando se o valor do depósito é positivo
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        # Verificando se o saque excede o saldo, o limite ou o número máximo de saques
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Opção de sair
    elif opcao == "4":
        break

    # Caso a opção informada seja inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
