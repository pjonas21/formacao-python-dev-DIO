saldo = 2000.0
saque = float(input("informe o valor para sacar: "))

if saldo >= saque:
    print("Realizando saque")
# desvio de controle
else:
    print("Saldo insuficiente")

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("informe o valor para sacar: "))
    if saldo >= saque:
        print("Realizando saque")
    # desvio de controle
    else:
        print("Saldo insuficiente")
elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção inválida.")



