balance = 0
limit = 500
bank_statement = ""
withdraws = 0
WITHDRAW_LIMIT = 3
BASE_ERROR = "Operação falhou!"

menu = """
    BEM VINDO AO GJBANK!
    
    SELECIONE UMA DAS SEGUINTES OPÇÕES:
  |-----------------|
  | [1] Extrato     |
  | [2] Sacar       |
  | [3] Depositar   |
  | [0] Sair        |
  |-----------------|

    => """

while True:

    option = input(menu)

    if option == "3":
        value = float(input("Informe o valor do depósito: "))

        if value > 0:
            balance += value
            bank_statement += f"Depósito: R$ {value:.2f}\n"
            print(
                f"""Depósito de R$ {value:.2f} realizado com sucesso!
---------------------------------------------\n"""
            )

        else:
            print(f"{BASE_ERROR} O valor informado é inválido.")

    elif option == "2":
        value = float(input("Informe o valor do saque: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdraws = withdraws >= WITHDRAW_LIMIT

        if exceeded_balance:
            print(f"{BASE_ERROR} Você não tem saldo suficiente.")

        elif exceeded_limit:
            print(f"{BASE_ERROR} O valor do saque excede o limite.")

        elif exceeded_withdraws:
            print(f"{BASE_ERROR} Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            bank_statement += f"Saque: R$ {value:.2f}\n"
            withdraws += 1
            print(
                f"""Saque de R$ {value:.2f} realizado com sucesso!
---------------------------------------------\n"""
            )

        else:
            print(f"{BASE_ERROR} O valor informado é inválido.")

    elif option == "1":
        print("\n================ EXTRATO ================")
        print(
            "Não foram realizadas movimentações."
            if not bank_statement
            else bank_statement
        )
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif option == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
