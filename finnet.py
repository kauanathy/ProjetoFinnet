# Listas para armazenar as contas a pagar e a receber
receivables = []
payables = []

def add_receivable(amount, description):
    receivables.append({"amount": amount, "description": description})
    print(f"Conta a Receber adicionada: {description} - R$ {amount:.2f}")

def add_payable(amount, description):
    payables.append({"amount": amount, "description": description})
    print(f"Conta a Pagar adicionada: {description} - R$ {amount:.2f}")

def view_receivables():
    print("\nContas a Receber:")
    if not receivables:
        print("Nenhuma conta a receber cadastrada.")
    for receivable in receivables:
        print(f"{receivable['description']}: R$ {receivable['amount']:.2f}")

def view_payables():
    print("\nContas a Pagar:")
    if not payables:
        print("Nenhuma conta a pagar cadastrada.")
    for payable in payables:
        print(f"{payable['description']}: R$ {payable['amount']:.2f}")

# Função principal para interação com o usuário
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Conta a Receber")
        print("2. Adicionar Conta a Pagar")
        print("3. Ver Contas a Receber")
        print("4. Ver Contas a Pagar")
        print("5. Sair")

        choice = input("Opção: ")

        if choice == '1':
            desc = input("Descrição da Conta a Receber: ")
            amount = float(input("Valor da Conta a Receber: "))
            add_receivable(amount, desc)
        elif choice == '2':
            desc = input("Descrição da Conta a Pagar: ")
            amount = float(input("Valor da Conta a Pagar: "))
            add_payable(amount, desc)
        elif choice == '3':
            view_receivables()
        elif choice == '4':
            view_payables()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa a função principal
if __name__ == "__main__":
    main()
